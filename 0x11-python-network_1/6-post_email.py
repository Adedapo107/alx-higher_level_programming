#!/usr/bin/python3
"""
    Script that takes in a URL and an email sends a POST request to that URL
    with the email as a parameter.
    Displays the body of the response
"""
import requests
from sys import argv


if __name__ == '__main__':
    payload = {'email': argv[2]}
    r = requests.post(argv[1], data=payload)
    print(r.text)
