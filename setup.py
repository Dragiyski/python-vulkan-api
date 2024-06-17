from setuptools import setup, Extension, Command
from setuptools.command.build import build
from setuptools.discovery import PackageFinder, PEP420PackageFinder

import pathlib, sys

# A lof ot hacky to handle the hackiness of PIP!
# This is not executed by python setup.py, it is executed by read() and exec() and setting __file__ to absolute path and __name__ to "__main__".
# Which means local includes from setup.py cannot work!

# There are 2 option, include all files code in registry to this file (bad)
# Rework the path, that should have been working by default...

project_dir = str(pathlib.Path(__file__).resolve().parent)
if project_dir not in sys.path:
    sys.path.append(project_dir)

from registry import GenerateVulkanSourceFiles


class BuildCommand(build):
    def run(self):
        self.run_command('vk_generate_source_files')
        self.distribution.packages = list(set((self.distribution.packages if self.distribution.packages is not None else []) + PEP420PackageFinder.find('src')))
        self.distribution.py_modules = list(set((self.distribution.py_modules if self.distribution.py_modules is not None else []) + PackageFinder.find('src')))
        build.run(self)


setup(
    cmdclass = {
        'vk_generate_source_files': GenerateVulkanSourceFiles,
        'build': BuildCommand
    },
    package_dir = {
        '': 'src'
    }
)
