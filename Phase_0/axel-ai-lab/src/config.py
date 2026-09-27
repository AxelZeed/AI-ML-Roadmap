import json
import logging
from pathlib import Path

import yaml

from src.models import Experiment


logger = logging.getLogger(
    "axel-ai-lab"
)


def load_json(
    file_path: str | Path,
) -> object:
    path = Path(file_path)

    with path.open(
        "r",
        encoding="utf-8",
    ) as file:
        return json.load(file)


def load_yaml(
    file_path: str | Path,
) -> object:
    path = Path(file_path)

    with path.open(
        "r",
        encoding="utf-8",
    ) as file:
        return yaml.safe_load(file)


def load_experiments(
    file_path: str | Path,
) -> list[Experiment]:
    path = Path(file_path)

    try:
        if path.suffix == ".json":
            experiments = load_json(path)

        elif path.suffix in {
            ".yaml",
            ".yml",
        }:
            config = load_yaml(path)

            if not isinstance(config, dict):
                logger.error(
                    "YAML root must be a mapping: %s",
                    path,
                )
                return []

            experiments = config[
                "experiments"
            ]

        else:
            logger.error(
                "Unsupported config format: %s",
                path,
            )
            return []

        if not isinstance(
            experiments,
            list,
        ):
            logger.error(
                "Experiments section must "
                "contain a list"
            )
            return []

        experiment_objects = []

        for experiment in experiments:
            if not isinstance(
                experiment,
                dict,
            ):
                logger.error(
                    "Experiment entry must "
                    "be a mapping"
                )
                continue

            experiment_objects.append(
                Experiment(**experiment)
            )

        return experiment_objects

    except FileNotFoundError:
        logger.error(
            "Config file not found: %s",
            path,
        )
        return []

    except json.JSONDecodeError as error:
        logger.error(
            "Invalid JSON in config file: %s",
            path,
        )
        logger.error(
            "JSON error details: %s",
            error,
        )
        return []

    except yaml.YAMLError as error:
        logger.error(
            "Invalid YAML in config file: %s",
            path,
        )
        logger.error(
            "YAML error details: %s",
            error,
        )
        return []

    except KeyError as error:
        logger.error(
            "Missing required config section: %s",
            error,
        )
        return []

    except TypeError as error:
        logger.error(
            "Invalid experiment "
            "configuration: %s",
            error,
        )
        return []