__version__ = '0.1.0'
from importlib_metadata import metadata
from loguru import logger


def main():
    """Initialize app."""
    logger.info(metadata(__package__).get('Name'))
    logger.info(metadata(__package__).get('Version'))
    logger.info(metadata(__package__).get('Summary'))
    logger.info(metadata(__package__).get('Home-page'))
    logger.info(metadata(__package__).get('Author'))
    logger.info(metadata(__package__).get('Author-email'))
