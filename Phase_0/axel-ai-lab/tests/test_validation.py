from src.models import Experiment
from src.validation import validate_experiment


def test_valid_experiment_passes_validation():
    experiment = Experiment(
        name="valid",
        sample_count=100,
        iterations=5,
        enabled=True,
    )

    assert validate_experiment(
        experiment
    ) is True


def test_invalid_sample_count_fails_validation():
    experiment = Experiment(
        name="invalid_samples",
        sample_count=0,
        iterations=5,
        enabled=True,
    )

    assert validate_experiment(
        experiment
    ) is False


def test_invalid_iterations_fail_validation():
    experiment = Experiment(
        name="invalid_iterations",
        sample_count=100,
        iterations=0,
        enabled=True,
    )

    assert validate_experiment(
        experiment
    ) is False


def test_empty_name_fails_validation():
    experiment = Experiment(
        name="",
        sample_count=100,
        iterations=5,
        enabled=True,
    )

    assert validate_experiment(
        experiment
    ) is False