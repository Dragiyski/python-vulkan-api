from setuptools import setup, Extension, Command
from registry import GenerateVulkanSourceFiles

setup(
    cmdclass={
        'vk_generate_source_files': GenerateVulkanSourceFiles
    },
    package_dir={
        '': 'src'
    }
)
