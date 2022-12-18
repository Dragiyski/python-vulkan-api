from setuptools import setup, Extension, Command
from registry import GenerateVulkanSourceFiles

setup(
    name="vulkan-ctypes",
    version="0.0.1",
    author="Plamen Dragiyski",
    author_email="plamen@dragiyski.org",
    cmdclass={
        'vk_generate_source_files': GenerateVulkanSourceFiles
    }
)
