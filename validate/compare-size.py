import ctypes
import tempfile
import subprocess
import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).parent.parent.joinpath('src').resolve()))

all = __import__('vulkan_api.ctypes').ctypes

template = """#include <stdio.h>
#include <vulkan/vulkan.h>

int main() {
    printf("%%s = %%lu", "%s", sizeof(%s));
    return 0;
}
"""


def get_code(name):
    return template % (name, name)


def get_struct_c_size(name, *, verbose=True):
    code = get_code(name)
    output_file = tempfile.NamedTemporaryFile(delete=False)
    output_file.close()
    compile_result = subprocess.run(['cc', '-x', 'c', '-o', output_file.name, '-'], input=code, encoding='utf-8', capture_output=True)
    if compile_result.returncode != 0:
        if verbose:
            print(compile_result.stderr, file=sys.stderr)
        return None
    chmod_result = subprocess.run(['chmod', 'u+x', output_file.name], capture_output=True)
    if chmod_result.returncode != 0:
        if verbose:
            print(compile_result.stderr, file=sys.stderr)
        return None
    exe_result = subprocess.run([output_file.name], capture_output=True)
    if exe_result.returncode != 0:
        if verbose:
            print(compile_result.stderr, file=sys.stderr)
        return None
    return exe_result.stdout.decode('ascii')


structures = {
    x: getattr(all, x)
    for x in dir(all)
    if isinstance(getattr(all, x), type) and (issubclass(getattr(all, x), ctypes.Structure) or issubclass(getattr(all, x), ctypes.Union))
}


def get_struct_py_size(name):
    return '%s = %d' % (name, ctypes.sizeof(structures[name]))


if __name__ == '__main__':
    for name in structures:
        csize = get_struct_c_size(name, verbose=False)
        if csize is None:
            print('Skip: %s' % name)
            continue
        pysize = get_struct_py_size(name)
        if csize != pysize:
            print('Diff: (C: %s), (Py: %s)' % (csize, pysize))
