url = 'https://raw.githubusercontent.com/KhronosGroup/Vulkan-Headers/main/'

file_list = [
    'registry/vk.xml',
    'registry/video.xml'
]

import pathlib, urllib.parse
from logging import getLogger
logger = getLogger('vulkan.registry')

def update(target):
    from ._http import fetch_file
    target = pathlib.Path(target).resolve()
    target.mkdir(parents=True, exist_ok=True)
    files = []
    for setup_file in file_list:
        source_url = urllib.parse.urljoin(url, setup_file)
        target_file = target.joinpath(setup_file)
        logger.debug(f'http.download: \n  url: {source_url}\n  file: {target_file}')
        status, reason, headers = fetch_file(target_file, source_url)
        if status == 0:
            logger.warning(f'http.download:\n  url: {source_url}\n  file: {target_file}\n  status: failed ({reason})\n  action: fallback to existing file')
        elif status == 304:
            logger.debug(f'http.download:\n  url: {source_url}\n  file: {target_file}\n  status: 304 Not Modified')
        elif status == 200:
            logger.debug(f'http.download:\n  url: {source_url}\n  file: {target_file}\n  status: 200 OK')
        files.append(target_file)
    return files
