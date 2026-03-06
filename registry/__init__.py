import pathlib
import os
import sys
import shutil
import urllib.parse
from .compiler import Compiler
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


class GenerateVulkanSourceFiles:
    def __init__(self, src_dir, dist_dir, var_dir):
        if isinstance(src_dir, str):
            src_dir = pathlib.Path(src_dir).resolve()
        if isinstance(dist_dir, str):
            dist_dir = pathlib.Path(dist_dir).resolve()
        if isinstance(var_dir, str):
            var_dir = pathlib.Path(var_dir).resolve()
        self.src_directory = src_dir
        self.dist_directory = dist_dir
        self.var_directory = var_dir
    
    def copy(self):
        for item in self.src_directory.iterdir():
            target = self.dist_directory / item.name
            if item.is_dir():
                shutil.copytree(item, target, dirs_exist_ok=True)
            else:
                shutil.copy2(item, target)

    def run(self):
        files = update(self.var_directory)
        package_dir = self.dist_directory.joinpath('dragiyski/vulkan/binding')
        generated_dir = package_dir.joinpath('_generated')
        generated_dir.mkdir(mode=0o755, parents=True, exist_ok=True)
        compiler = Compiler()
        for file in files:
            compiler.add_xml_file(file)
        context = compiler.compile()
        generator = Generator(generated_dir)
        generator.generate(context)
        self.copy()
