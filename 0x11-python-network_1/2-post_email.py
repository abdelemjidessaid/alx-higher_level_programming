#!/usr/bin/python3
"""
Script that:
    - takes in a URL
    - and email
    - sends a POST request to the passed URL with the email as a parameter
    - displays the body of the response (decoded in utf-8)
"""

import sys
import urllib.request
import urllib.parse


if __name__ == '__main__':
    # get passed info
    url = sys.argv[1]
    email = sys.argv[2]
    # parse info
    data = urllib.parse.urlencode({'email': email}).encode('ascii')
    # make request for post method
    request = urllib.request.Request(url=url, data=data)
    # get the response
    with urllib.request.urlopen(request) as res:
        print(res.read().decode('utf-8'))
