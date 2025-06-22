# utils/logger.py
"""
Simple logging utility module.
Provides get_logger to create or retrieve a configured logger.
"""
import logging
import sys


def get_logger(name: str, level: str = 'INFO') -> logging.Logger:
    """
    Get a logger with the specified name and level, configured to output to stdout.

    :param name: Name of the logger.
    :param level: Logging level as a string (e.g., 'DEBUG', 'INFO', 'WARNING').
    :return: Configured Logger instance.
    """
    # Convert level string to logging level
    numeric_level = getattr(logging, level.upper(), logging.INFO)

    logger = logging.getLogger(name)
    # Avoid adding multiple handlers if already configured
    if not logger.handlers:
        logger.setLevel(numeric_level)
        # Create console handler
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(numeric_level)
        # Define formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        # Prevent log messages from propagating to root logger
        logger.propagate = False

    return logger
