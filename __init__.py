import json
import sys
import os


def get_api_key():
    try:
        with open("config.json", "r") as settings:
            return json.loads(settings.read())["key1"]
    except FileNotFoundError:
        raise FileNotFoundError(
            "You may not have created a `config.json` file. See LAB_SETUP.md for instructions."
        )
