from src.models import Experiment, ExperimentResult


def run_experiment(
    experiment: Experiment,
) -> ExperimentResult:
    score = (
        experiment.learning_rate
        * experiment.epochs
        * 100
    )

    print(f"Running: {experiment.name}")
    print(f"Learning rate: {experiment.learning_rate}")
    print(f"Epochs: {experiment.epochs}")
    print(f"Score: {score}")

    return ExperimentResult(
        name=experiment.name,
        score=score,
    )