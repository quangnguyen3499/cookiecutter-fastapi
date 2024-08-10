from typing import Dict

import yaml

from core.loggers.app_logging import logger


def load_yaml_template(yaml_file: str) -> Dict:
    """
    Load YAML template from a file.
    """
    try:
        with open(yaml_file, "r") as file:
            return yaml.safe_load(file)
    except IOError as e:
        logger.error(f"Error opening YAML file: {e}")
        return {}


def load_example_yaml_template(yaml_file: str) -> Dict:
    """
    Load example YAML template from a .yaml file
    """
    try:
        with open(yaml_file, "r") as file:
            # Load the YAML file
            data = yaml.safe_load(file)
            load_examples = {}

            # Parsing each stage's content into a list of strings
            for stage, content in data.items():
                # Split the content by newline and remove empty lines
                load_examples[stage] = [
                    line.strip() for line in content.split("\n") if line.strip()
                ]

        return load_examples
    except IOError as e:
        logger.error(f"Error opening YAML file: {e}")
        return {}
