import re
import requests

def get_bedrock_server_latest_version() -> str:
    timeout = 3
    useragent = 'aoirint/pymcversion'
    headers = {
        'User-Agent': useragent,
    }

    res = requests.get('https://www.minecraft.net/en-us/download/server/bedrock', headers=headers, timeout=timeout)
    html = res.text

    # https://minecraft.azureedge.net/bin-linux/bedrock-server-1.17.40.06.zip
    m = re.search(r'"https://minecraft\.azureedge\.net/bin-linux/bedrock-server-(.+?)\.zip"', html)
    if m is None:
        raise Exception('No match found. URL or filename changed?')

    version = m.group(1)
    return version
