#!/usr/bin/python3
"""
Script that:
    - takes in a URL
    - sends a request to the URL
    - displays the body of the response (decoded in utf-8).
Usage:
    ./3-error_code.py url
"""

import sys
import urllib.request
import urllib.error


if __name__ == '__main__':
    url = sys.argv[1]
    with urllib.request.Request(url) as request:
        try:
            result = urllib.request.urlopen(request)
            print(result)
        except urllib.error.HTTPError as e:
            print('Error code: {}'.format(e.code))
