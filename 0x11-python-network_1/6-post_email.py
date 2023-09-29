#!/usr/bin/python3
"""
Script that:
    - takes in a URL
    - an email address
    - sends a POST request to the passed URL with the email as a parameter
    - finally displays the body of the response.
Usage:
    ./6-post_email.py <URL> <EMAIL>
"""

if __name__ == '__main__':
    import sys
    import requests

    url = sys.argv[1]
    email = sys.argv[2]
    res = requests.post(url=url, data={'email': email})
    print(res.text)
