from collections.abc import Iterator

from src.models import Experiment


def generate_experiment_sweep(
    sample_counts: list[int],
    iteration_values: list[int],
) -> Iterator[Experiment]:
    for sample_count in sample_counts:
        for iterations in iteration_values:
            yield Experiment(
                name=(
                    f"samples_{sample_count}"
                    f"_iterations_{iterations}"
                ),
                sample_count=sample_count,
                iterations=iterations,
                enabled=True,
            )