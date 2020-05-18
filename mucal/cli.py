import argparse
import requests
import icalendar
import sys


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("outfile")
    args = parser.parse_args()
    print(args)
