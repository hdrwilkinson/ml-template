import argparse
import yaml
from pathlib import Path

from utils import logging

def load_config(config_path):
    """
    Loads the YAML configuration file.
    """
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def parse_arguments():
    """
    Parses command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Training Script Configuration")
    parser.add_argument('config', type=str, help='Path to the configuration YAML file')
    return parser.parse_args()

def main():
    # Parse command-line arguments
    args = parse_arguments()
    
    # Load configuration
    config = load_config(args.config)
    
    # Set up logging
    logger = logging.setup_logging(config)
    
    # Log the loaded configuration in flattened format
    logging.log_config(config, logger)
    
    # Template section
    logging.log_section(logger, "Section Header")
    logger.info("Informational message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.critical("Critical message")

if __name__ == "__main__":
    main()
