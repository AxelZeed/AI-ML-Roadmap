from src.models import Experiment


def find_experiment(
    experiments: list[Experiment],
    name: str,
) -> Experiment | None:
    for experiment in experiments:
        if experiment.name == name:
            return experiment

    return None

def build_experiment_index(
    experiments: list[Experiment],
) -> dict[str, Experiment]:
    return {
        experiment.name: experiment
        for experiment in experiments
    }