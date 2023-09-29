#!/usr/bin/python3
"""
Script that:
    - takes in a URL
    - sends a request to the URL
    - displays the value of the variable `X-Request-Id`
      in the response header
Usage:
    ./5-tbtn_header.py url
"""

import sys
import requests


if __name__ == '__main__':
    url = sys.argv[1]
    res = requests.get(url)
    result = res.headers.get('X-Request-Id')
    print(result)
