import logging
from src.models import Experiment

logger = logging.getLogger("axel-ai-lab")


def validate_experiment(
    experiment: Experiment,
) -> bool:
    if not isinstance(experiment.name, str):
        logger.error("Experiment name must be a string")
        return False

    if not isinstance(
        experiment.learning_rate,
        (int, float),
    ):
        logger.error(
            "Learning rate must be a number for experiment: %s",
            experiment.name,
        )
        return False

    if not isinstance(experiment.epochs, int):
        logger.error(
            "Epochs must be an integer for experiment: %s",
            experiment.name,
        )
        return False

    if not isinstance(experiment.enabled, bool):
        logger.error(
            "Enabled must be a boolean for experiment: %s",
            experiment.name,
        )
        return False

    return True