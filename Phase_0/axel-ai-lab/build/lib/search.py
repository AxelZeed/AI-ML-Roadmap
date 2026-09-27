from src.models import Experiment


def find_experiment(
    experiments: list[Experiment],
    name: str,
) -> Experiment | None:
    for experiment in experiments:
        if experiment.name == name:
            return experiment

    return None