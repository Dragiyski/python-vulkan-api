from setuptools import setup, Extension, Command
from setuptools.command.build import build
from setuptools.discovery import PackageFinder, PEP420PackageFinder
from registry import GenerateVulkanSourceFiles

class BuildCommand(build):
    def run(self):
        self.run_command('vk_generate_source_files')
        self.distribution.packages = list(set((self.distribution.packages if self.distribution.packages is not None else []) + PEP420PackageFinder.find('src')))
        self.distribution.py_modules = list(set((self.distribution.py_modules if self.distribution.py_modules is not None else []) + PackageFinder.find('src')))
        build.run(self)

setup(
    cmdclass={
        'vk_generate_source_files': GenerateVulkanSourceFiles,
        'build': BuildCommand
    },
    package_dir={
        '': 'src'
    }
)
