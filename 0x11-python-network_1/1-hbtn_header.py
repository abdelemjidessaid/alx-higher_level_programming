#!/usr/bin/python3
"""
Script that:
    - takes in a URL
    - sends a request to the URL
    - displays the value of the X-Request-Id variable found in the header of the response.
"""

import sys
import urllib.request


if __name__ == '__main__':
    # get the url passed.
    url = sys.argv[1]
    # request the content.
    request = urllib.request.Request(url)
    # filter the content and get the header of `X-Request-Id`
    with urllib.request.urlopen(request) as res:
        print(dict(res.headers)['X-Request-Id'])
