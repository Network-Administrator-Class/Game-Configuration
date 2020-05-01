"""
Configuration file handling with JSON.
"""

import json


def show(settings):
    """Print configuration data."""
    print("\n\nDEBUG: SAVED CONFIGURATION:\n")
    if settings != {}:
        for setting, value in settings.items():
            print(setting, ":", value)
    else:
        print("No configuration found.")


def load(filename):
    """Load configuration data from file."""
    try:
        cfg = open(filename, "r")
        settings = json.load(cfg)
        cfg.close()
        return settings
    except FileNotFoundError:
        return {"money": 1000}


def save(settings, filename):
    """Save configuration data to file."""
    cfg = open(filename, "w")
    json.dump(settings, cfg)

