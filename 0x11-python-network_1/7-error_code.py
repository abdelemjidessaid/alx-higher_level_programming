#!/usr/bin/python3
"""
Script that:
    - takes in a URL
    - sends a request to the URL and displays the body of the response.
Usage:
    ./7-error_code.py URL.
"""

if __name__ == '__main__':
    import sys
    import requests

    try:
        res = requests.get(sys.argv[1])
        print(res.text)
    except requests.HTTPError as e:
        if (e.errno >= 400):
            print('Error code: {}'.format(e.errno))
