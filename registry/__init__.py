import pathlib
import os
import urllib.parse
from setuptools import Command
from .generator import Generator

repository_url = 'https://raw.githubusercontent.com/KhronosGroup/Vulkan-Headers/main/'

setup_files = [
    'registry/vk.xml',  # The main registry, containing the basic structure data
    'registry/video.xml',  # The supplementary registry for video encode/decode
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
        # generator = Generator()
        # for file in files:
        #    generator.add_xml_file(file)
        from .code import CPreprocessor
        preprocessor = CPreprocessor()
        code = """#ifndef VK_DEFINE_NON_DISPATCHABLE_HANDLE
    #if (VK_USE_64_BIT_PTR_DEFINES==1)
        #if (defined(__cplusplus) && (__cplusplus >= 201103L)) || (defined(_MSVC_LANG) && (_MSVC_LANG >= 201103L))
            #define VK_NULL_HANDLE nullptr
            if (some > conditional) {
                code;
            }
        #else
            #define VK_NULL_HANDLE \\
                ((void*)0)
        #endif
    #else
        #define VK_NULL_HANDLE 0ULL
    #endif
#endif
#ifndef VK_NULL_HANDLE
    #define VK_NULL_HANDLE 0
#endif"""
        preprocessor.process(code)
        j = 0
