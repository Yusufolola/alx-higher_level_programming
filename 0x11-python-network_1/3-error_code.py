#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the body of the
response (decoded in utf-8).
"""
import urllib.request
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")