import sys, os, logging, pathlib, urllib.parse, urllib.request
from datetime import datetime, timezone
from logging import getLogger
from setuptools import Command, Distribution
from ._http import fetch_file

class VulkanRegistryDownloadCommand(Command):
    vulkan_repository_url = 'https://raw.githubusercontent.com/KhronosGroup/Vulkan-Headers/main/'

    vulkan_setup_files = [
        'registry/vk.xml',  # The main registry, containing the basic structure data
        'registry/video.xml',  # The supplementary registry for video encode/decode
    ]

    description = 'download vulkan header registry files'

    user_options = [
        ('target-dir=', None, 'specify the target directory for download'),
    ]

    def initialize_options(self) -> None:
        self.logger = getLogger('vulkan.registry')
        self.target_dir = pathlib.Path(__file__).resolve().parent.parent.joinpath('var')

    def finalize_options(self) -> None:
        self.target_dir = pathlib.Path(self.target_dir).resolve()
        if self.distribution.verbose:
            self.logger.setLevel(logging.INFO)
        else:
            self.logger.setLevel(logging.CRITICAL)
    
    def run(self) -> None:
        failure = None
        for file in self.vulkan_setup_files:
            source_url = urllib.parse.urljoin(self.vulkan_repository_url, file)
            target_file = self.target_dir.joinpath(file)
            self.logger.info(f'download [{source_url}] into "{target_file}"')
            status, reason, headers = fetch_file(target_file, source_url)
            if status == 304:
                self.logger.info(f'download [{source_url}] skipped: file "{target_file}" already up-to-date')
            elif status == 200:
                self.logger.info(f'download [{source_url}] successful: file "{target_file}" updated')
            else:
                if target_file.exists():
                    log_error = self.logger.warning
                else:
                    log_error = self.logger.critical
                    if failure is None:
                        failure = RuntimeError(f'Unable to retrieve a registry file from {source_url}')
                log_error(f'download [{source_url}] failed: {status} {reason}')
        if failure is not None:
            raise failure
