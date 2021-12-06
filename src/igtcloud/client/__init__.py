try:
    from .__version__ import version as __version__
except ImportError:
    # Fallback, used only for testing without installing library
    __version__ = '0.0.0'
