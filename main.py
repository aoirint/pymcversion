import re
import requests

timeout = 3
useragent = 'aoirint/minecraft-bedrock-server-version'
headers = {
    'User-Agent': useragent,
}

res = requests.get('https://www.minecraft.net/en-us/download/server/bedrock', headers=headers, timeout=timeout)
html = res.text

# https://minecraft.azureedge.net/bin-linux/bedrock-server-1.17.40.06.zip
m = re.search(r'"https://minecraft\.azureedge\.net/bin-linux/bedrock-server-(.+?)\.zip"', html)

version = m.group(1)

print(version)
