import ctypes
import re
from collections.abc import Iterable, Mapping


def make_array_ptr_from_iterable(ctype, iterable: Iterable):
    iterable = list(iterable)
    count = len(iterable)
    if count <= 0:
        return None
    array = (ctype * count)()
    for i in range(count):
        array[i] = iterable[i]
    return ctypes.cast(array, ctypes.POINTER(ctype))

def make_c_string_list(iterable: Iterable):
    return list(s.encode() if isinstance(s, str) else s for s in iterable)

def make_python_name(name, *, p = False, s = True):
        words = name.split('_')
        words = [re.findall(r'(?:[A-Z][A-Z0-9]*|^)[a-z0-9]*', word) for word in words]
        words = [word.lower() for x in words for word in x]
        if p and len(words) > 1 and re.fullmatch(r'p+', words[0]):
            words = words[1:]
        elif s and len(words) > 1 and re.fullmatch(r's+', words[0]):
            words = words[1:]
        return '_'.join(words)

def extend_namespace(*args, **kwargs):
    def class_body(namespace):
        for arg in args:
            if not isinstance(arg, Mapping):
                raise TypeError('Expected every positional arguments to be a mapping')
            namespace.update(arg)
        namespace.update(kwargs)
        namespace['__dict__'] = namespace
    return class_body