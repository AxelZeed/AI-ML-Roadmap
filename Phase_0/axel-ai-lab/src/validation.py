import logging

from src.models import Experiment


logger = logging.getLogger("axel-ai-lab")


def validate_experiment(
    experiment: Experiment,
) -> bool:
    if not isinstance(experiment.name, str):
        logger.error(
            "Experiment name must be a string"
        )
        return False

    if not experiment.name.strip():
        logger.error(
            "Experiment name cannot be empty"
        )
        return False

    if not isinstance(
        experiment.sample_count,
        int,
    ):
        logger.error(
            "sample_count must be an integer for experiment: %s",
            experiment.name,
        )
        return False

    if experiment.sample_count <= 0:
        logger.error(
            "sample_count must be greater than zero for experiment: %s",
            experiment.name,
        )
        return False

    if not isinstance(
        experiment.iterations,
        int,
    ):
        logger.error(
            "iterations must be an integer for experiment: %s",
            experiment.name,
        )
        return False

    if experiment.iterations <= 0:
        logger.error(
            "iterations must be greater than zero for experiment: %s",
            experiment.name,
        )
        return False

    if not isinstance(
        experiment.enabled,
        bool,
    ):
        logger.error(
            "enabled must be a boolean for experiment: %s",
            experiment.name,
        )
        return False

    return True