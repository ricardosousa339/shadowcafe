import os

def get_asset_path(filename):
    return os.path.join(os.path.dirname(__file__), 'assets', filename)