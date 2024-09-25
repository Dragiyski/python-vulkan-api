import os
import pathlib
from datetime import datetime, timezone
import urllib.request

HTTP_DATE_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'


def fetch_file(target_file, source_url):
    target_file = pathlib.Path(target_file)
    target_file.parent.mkdir(parents=True, exist_ok=True)
    headers = {
        'Date': datetime.now(timezone.utc).strftime(HTTP_DATE_FORMAT)
    }
    has_file = True
    try:
        stat = os.stat(target_file)
        headers['if-modified-since'] = datetime.fromtimestamp(stat.st_mtime, timezone.utc).strftime(HTTP_DATE_FORMAT)
    except FileNotFoundError:
        has_file = False
    etag_path = target_file.parent.joinpath(f'.{target_file.name}.etag')
    try:
        with open(etag_path, 'r') as file:
            headers['if-none-match'] = file.read()
    except FileNotFoundError:
        pass
    req = urllib.request.Request(url=source_url, headers=headers, method='GET')
    try:
        res = urllib.request.urlopen(url=req)
    except urllib.request.HTTPError as error:
        if error.code != 304:
            raise
        if 'etag' in error.headers:
            with open(etag_path, 'w') as file:
                file.write(error.headers['etag'])
        return (error.code, error.reason, error.headers)
    except urllib.request.URLError as e:
        if not has_file:
            raise
        return (0, e.strerror, {})
    try:
        if 'etag' in res.headers:
            with open(etag_path, 'w') as file:
                file.write(res.headers['etag'])
        data = res.read()
        with open(target_file, 'wb') as file:
            file.write(data)
    finally:
        res.close()
    return (res.status, res.reason, res.headers)
