import pathlib
import os
import urllib.parse
from setuptools import Command
from ._parser import RegistryParser
from ._model import Model

repository_url = 'https://raw.githubusercontent.com/KhronosGroup/Vulkan-Headers/main/'

setup_files = [
    'registry/vk.xml',  # The main registry, containing the basic structure data;
    'registry/video.xml',  # The supplementary registry for video encode/decode
    'include/vulkan/vk_platform.h',  # Header containing the calling convention for the C functions
]


def update(target):
    from ._http import fetch_file
    target = pathlib.Path(target).resolve()
    target.mkdir(parents=True, exist_ok=True)
    files = []
    for setup_file in setup_files:
        source_url = urllib.parse.urljoin(repository_url, setup_file)
        target_file = target.joinpath(setup_file)
        files.append(fetch_file(target_file, source_url))
    return files


class GenerateVulkanTypeValidationFiles(Command):
    user_options = [
        ('vk-dir=', None, 'Vulkan Headers registry directory')
    ]
    
    def initialize_options(self):
        self.vk_directory = pathlib.Path(os.getcwd()).resolve().joinpath('var/vulkan-headers')
        
    def finalize_options(self):
        if self.vk_directory:
            if not isinstance(self.vk_directory, pathlib.Path):
                self.vk_directory = pathlib.Path(self.vk_directory)
    
    def run(self):
        # print('Hello from command')
        from pprint import pformat
        files = update(self.vk_directory)
        print('Updaring registring:\n - target: %s\n - files: %s' % (str(self.vk_directory), pformat(files)))
        parser = Model(*[x for x in files if str(x).endswith('.xml')])
        j = 0
