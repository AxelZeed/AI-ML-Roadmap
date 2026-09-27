import json
import logging

import yaml
from src.models import Experiment

logger = logging.getLogger("axel-ai-lab")


def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def load_yaml(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def load_experiments(
    file_path: str,
) -> list[Experiment]:
    try:
        if file_path.endswith(".json"):
            experiments = load_json(file_path)

        elif file_path.endswith(".yaml") or file_path.endswith(".yml"):
            config = load_yaml(file_path)
            experiments = config["experiments"]

        else:
            logger.error(
                "Unsupported config format: %s",
                file_path,
            )
            return []

        experiment_objects = []

        for experiment in experiments:
            experiment_objects.append(
                Experiment(**experiment)
            )

        return experiment_objects

    except FileNotFoundError:
        logger.error(
            "Config file not found: %s",
            file_path,
        )
        return []

    except json.JSONDecodeError as error:
        logger.error(
            "Invalid JSON in config file: %s",
            file_path,
        )
        logger.error("JSON error details: %s", error)
        return []

    except yaml.YAMLError as error:
        logger.error(
            "Invalid YAML in config file: %s",
            file_path,
        )
        logger.error("YAML error details: %s", error)
        return []

    except KeyError as error:
        logger.error(
            "Missing required YAML section: %s",
            error,
        )
        return []
        
    except TypeError as error:
        logger.error(
            "Invalid experiment configuration: %s",
            error,
        )
        return []