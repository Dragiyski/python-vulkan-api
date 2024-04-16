import pathlib
import os
import sys
from datetime import datetime, timezone
import urllib.parse
from setuptools import Command
from .compiler import Parser

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
        print(f'Downloading file:\n - URL: {source_url}\n - File: {target_file}', file=sys.stderr)
        status, reason, headers = fetch_file(target_file, source_url)
        if status == 0:
            print(' - Status: Not updated, failure: %s' % (reason), file=sys.stderr)
        elif status == 304:
            print(' - Status: Already up-to-date', file=sys.stderr)
        elif status == 200:
            print(' - Status: File updated', file=sys.stderr)
        files.append(target_file)
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
        files = update(self.vk_directory)
        project_dir = pathlib.Path(__file__).resolve().parent.parent
        src_dir = project_dir.joinpath('src')
        package_dir = src_dir.joinpath('dragiyski/lib/vulkan')
        parser = Parser()
        for file in files:
            parser.add_xml_file(file)
        parser.compile()

        # enum_source = generator.generate_enum_source()
        # with open(enum_source_file, 'w') as file:
        #     file.write(enum_source)
        # del enum_source
        # bitmask_source = generator.generate_bitmask_source()
        # with open(bitmask_source_file, 'w') as file:
        #     file.write(bitmask_source)
        # del bitmask_source
        # const_source = generator.generate_const_source()
        # with open(const_source_file, 'w') as file:
        #     file.write(const_source)
        # del const_source
        # values_source = generator.generate_value_source()
        # with open(vk_values_source_file, 'w') as file:
        #     file.write(values_source)
        # del values_source
        # type_source = generator.generate_type_source()
        # with open(ctype_struct_source_file, 'w') as file:
        #     file.write(type_source)
        # del type_source
        # cmd_source = generator.generate_command_source()
        # with open(ctype_cmd_source_file, 'w') as file:
        #     file.write(cmd_source)
        # del cmd_source
        # project_dir = pathlib.Path(__file__).resolve().parent.parent
        # src_dir = project_dir.joinpath('src')
        # package_dir = src_dir.joinpath('vulkan_api')
        # package_dir.mkdir(mode=0o755, exist_ok=True, parents=True)
        # with open(package_dir.joinpath('ctypes.py'), 'w') as file:
        #     file.write(combined_source)