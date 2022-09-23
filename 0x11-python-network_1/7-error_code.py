#!/usr/bin/python3
"""
    Script that takes in a URL sends a POST request to that URL
    Displays the body of the response
"""
import requests
import sys


if __name__ == '__main__':
    r = requests.get(argv[1])
    status = r.status_code
    print(r.text) if status < 400 else print(
        "Error code: {}".format(r.status_code))
