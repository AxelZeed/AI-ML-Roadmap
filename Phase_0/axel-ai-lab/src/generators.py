import logging
from collections.abc import Iterator

from src.models import Experiment
from src.validation import validate_experiment


logger = logging.getLogger("axel-ai-lab")


def iter_runnable_experiments(
    experiments: list[Experiment],
) -> Iterator[Experiment]:
    for experiment in experiments:
        if not validate_experiment(experiment):
            logger.error(
                "Skipping invalid experiment"
            )
            continue

        if not experiment.enabled:
            logger.warning(
                "Skipping disabled experiment: %s",
                experiment.name,
            )
            continue

        yield experiment

def batched(
    items: list[Experiment],
    batch_size: int,
) -> Iterator[list[Experiment]]:
    for start_index in range(
        0,
        len(items),
        batch_size,
    ):
        yield items[
            start_index:
            start_index + batch_size
        ]