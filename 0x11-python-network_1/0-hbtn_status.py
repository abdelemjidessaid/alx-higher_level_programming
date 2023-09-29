#!/usr/bin/python3
"""
    Status module, for fetching a URL.
"""

import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
    html = res.read()
    print(html)
