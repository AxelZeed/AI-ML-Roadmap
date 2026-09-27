from src.models import Experiment
from src.search import (
    build_experiment_index,
    find_experiment,
)


def test_find_experiment_returns_matching_experiment():
    experiments = [
        Experiment(
            name="alpha",
            sample_count=100,
            iterations=5,
            enabled=True,
        ),
        Experiment(
            name="beta",
            sample_count=200,
            iterations=10,
            enabled=True,
        ),
    ]

    result = find_experiment(
        experiments,
        "beta",
    )

    assert result is not None
    assert result.name == "beta"


def test_find_experiment_returns_none_when_missing():
    experiments = [
        Experiment(
            name="alpha",
            sample_count=100,
            iterations=5,
            enabled=True,
        ),
    ]

    result = find_experiment(
        experiments,
        "missing",
    )

    assert result is None


def test_build_experiment_index_maps_names_to_objects():
    experiments = [
        Experiment(
            name="alpha",
            sample_count=100,
            iterations=5,
            enabled=True,
        ),
        Experiment(
            name="beta",
            sample_count=200,
            iterations=10,
            enabled=True,
        ),
    ]

    index = build_experiment_index(
        experiments
    )

    assert (
        index["alpha"].sample_count
        == 100
    )

    assert (
        index["beta"].iterations
        == 10
    )