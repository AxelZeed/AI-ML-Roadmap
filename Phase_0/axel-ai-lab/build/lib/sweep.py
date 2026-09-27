from collections.abc import Iterator

from src.models import Experiment


def generate_experiment_sweep(
    learning_rates: list[float],
    epoch_values: list[int],
) -> Iterator[Experiment]:
    for learning_rate in learning_rates:
        for epochs in epoch_values:
            yield Experiment(
                name=(
                    f"lr_{learning_rate}_epochs_{epochs}"
                ),
                learning_rate=learning_rate,
                epochs=epochs,
                enabled=True,
            )