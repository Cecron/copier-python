import importlib.metadata

if __package__ is None:
    __version__ = "0.0.0"
else:
    __version__ = importlib.metadata.version(__package__)
