import os


def mk(path):
    os.makedirs(path, exist_ok=True)
