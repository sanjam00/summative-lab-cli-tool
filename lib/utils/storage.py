import os
import json

def load_settings(filepath="./settings.json"):
  if os.path.exists(filepath):
    try:
      with open(filepath, "r") as file:
        return json.load(file)
    except (json.JSONDecodeError, IOError):
      pass
  return {}

def get_setting(key, default=None):
  settings = load_settings()
  return settings.get(key, default)