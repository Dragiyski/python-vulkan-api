import sys, pathlib
from setuptools import setup

project_dir = str(pathlib.Path(__file__).resolve().parent)
if project_dir not in sys.path:
    sys.path.append(project_dir)

from registry.download import VulkanRegistryDownloadCommand
from registry.generate import VulkanRegistryGenerateCommand

setup(
    cmdclass = {
        'vk_registry_download': VulkanRegistryDownloadCommand,
        'vk_registry_generate': VulkanRegistryGenerateCommand
    },
    package_dir = {
        '': 'src'
    }
)