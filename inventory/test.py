#!/usr/bin/env python

import argparse
import requests
import datetime
from datetime import date


try:
    import json
except ImportError:
    import simplejson as json


class Inventory(object):

    def __init__(self):

        self.parse_cli_args()

        self.inventory = {}

        if self.args.list:
            self.handle_list()

        print(json.dumps(self.inventory))

    def handle_list(self):

        atlassian = {
            "url": "http://localhost",
            "username": "my-username",
            "password": "my-password",
        }

        self.inventory = atlassian

    def parse_cli_args(self):
        parser = argparse.ArgumentParser(
            description='Produce an Ansible Inventory from a file')
        parser.add_argument('--list', action='store_true')
        parser.add_argument('--host', action='store')
        self.args = parser.parse_args()


Inventory()
