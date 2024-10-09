import logging
import os
from pathlib import Path
from itertools import groupby

def setup_logging(config):
    """
    Sets up logging based on the provided configuration.
    """
    logging_config = config.get('logging', {})
    
    # Define default logging settings
    level = logging_config.get('level', 'INFO').upper()
    format = logging_config.get('format', "%(asctime)s - %(levelname)s - %(message)s")
    datefmt = logging_config.get('datefmt', "%Y-%m-%d %H:%M:%S")
    log_file = logging_config.get('file', "logging/train.log")
    
    # Ensure the logging directory exists
    log_path = Path(log_file)
    log_dir = log_path.parent
    log_dir.mkdir(parents=True, exist_ok=True)
    
    logging.basicConfig(
        level=level,
        format=format,
        datefmt=datefmt,
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(log_file),
        ],
    )
    logger = logging.getLogger(__name__)
    return logger

def flatten_config(config, parent_key='', sep='.'):
    """
    Flattens a nested dictionary.
    """
    items = {}
    for k, v in config.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_config(v, new_key, sep=sep))
        else:
            items[new_key] = v
    return items

def log_section(logger, section_name, width=79):
    """
    Logs a section separator with the given name.
    
    Args:
        logger (logging.Logger): The logger instance.
        section_name (str): The name of the section.
        width (int): The total width of the separator (default is 79 for PEP 8 compliance).
    """
    separator = "=" * width
    padding = "=" * ((width - len(section_name) - 2) // 2)
    section_line = f"{padding} {section_name.upper()} {padding}"
    if len(section_line) < width:
        section_line += "="
    
    logger.info("")
    logger.info(separator)
    logger.info(section_line)
    logger.info(separator)

def log_config(config, logger):
    """
    Logs the configuration grouped by highest-level elements.
    Each section is capitalized and has a clear line below.
    """
    log_section(logger, "Config")
    flattened_config = flatten_config(config)
    
    # Group by the highest-level element
    grouped_config = groupby(sorted(flattened_config.items()), key=lambda x: x[0].split('.')[0])
    
    for group, items in grouped_config:
        logger.info(f"{group.upper()}:")
        for key, value in items:
            logger.info(f"  {key} = {value}")
        logger.info("")  # Clear line below each section