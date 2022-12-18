import pathlib
import os
import sys
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


class GenerateVulkanSourceFiles(Command):
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
        print('Updaring registring:\n - target: %s\n - files: %s' % (str(self.vk_directory), pformat(files)), file=sys.stderr)
        generator = Generator()
        for file in files:
            generator.add_xml_file(file)
        generator.compile()
        combined_source = generator.generate_combined_source()
        project_dir = pathlib.Path(__file__).resolve().parent.parent
        src_dir = project_dir.joinpath('src')
        package_dir = src_dir.joinpath('vulkan_api')
        package_dir.mkdir(mode=0o755, exist_ok=True, parents=True)
        with open(package_dir.joinpath('ctypes.py'), 'w') as file:
            file.write(combined_source)
