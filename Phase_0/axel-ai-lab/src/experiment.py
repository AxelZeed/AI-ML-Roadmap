import math
import time
from datetime import datetime

from src.models import (
    Experiment,
    ExperimentResult,
)
from src.run_id import generate_run_id


def run_experiment(
    experiment: Experiment,
) -> ExperimentResult:
    run_id = generate_run_id()

    started_at = datetime.now().isoformat(
        timespec="seconds"
    )

    start_time = time.perf_counter()

    total = 0.0

    for iteration in range(
        experiment.iterations
    ):
        iteration_total = 0.0

        for value in range(
            1,
            experiment.sample_count + 1,
        ):
            iteration_total += math.sqrt(
                value
            )

        total += iteration_total

    score = (
        total
        / experiment.iterations
        / experiment.sample_count
    )

    duration_seconds = (
        time.perf_counter()
        - start_time
    )

    finished_at = datetime.now().isoformat(
        timespec="seconds"
    )

    print(
        f"Run ID: {run_id}"
    )
    print(
        f"Running: {experiment.name}"
    )
    print(
        f"Samples: {experiment.sample_count}"
    )
    print(
        f"Iterations: {experiment.iterations}"
    )
    print(
        f"Score: {score:.6f}"
    )
    print(
        f"Duration: "
        f"{duration_seconds:.6f} seconds"
    )

    return ExperimentResult(
        run_id=run_id,
        name=experiment.name,
        score=score,
        duration_seconds=duration_seconds,
        started_at=started_at,
        finished_at=finished_at,
        status="success",
    )