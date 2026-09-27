from src.generators import (
    batched,
    iter_runnable_experiments,
)
from src.models import Experiment


def test_iter_runnable_experiments_skips_disabled():
    experiments = [
        Experiment(
            name="enabled",
            sample_count=100,
            iterations=5,
            enabled=True,
        ),
        Experiment(
            name="disabled",
            sample_count=100,
            iterations=5,
            enabled=False,
        ),
    ]

    runnable = list(
        iter_runnable_experiments(
            experiments
        )
    )

    assert len(runnable) == 1
    assert runnable[0].name == "enabled"


def test_iter_runnable_experiments_skips_invalid():
    experiments = [
        Experiment(
            name="valid",
            sample_count=100,
            iterations=5,
            enabled=True,
        ),
        Experiment(
            name="invalid",
            sample_count=0,
            iterations=5,
            enabled=True,
        ),
    ]

    runnable = list(
        iter_runnable_experiments(
            experiments
        )
    )

    assert len(runnable) == 1
    assert runnable[0].name == "valid"


def test_batched_splits_experiments_into_groups():
    experiments = [
        Experiment(
            name="one",
            sample_count=10,
            iterations=1,
            enabled=True,
        ),
        Experiment(
            name="two",
            sample_count=10,
            iterations=1,
            enabled=True,
        ),
        Experiment(
            name="three",
            sample_count=10,
            iterations=1,
            enabled=True,
        ),
    ]

    batches = list(
        batched(
            experiments,
            batch_size=2,
        )
    )

    assert len(batches) == 2
    assert len(batches[0]) == 2
    assert len(batches[1]) == 1