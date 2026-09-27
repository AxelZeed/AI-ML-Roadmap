from src.comparison import (
    get_best_result,
    get_fastest_result,
    get_slowest_result,
)
from src.models import ExperimentResult


def print_summary(
    total_experiments: int,
    completed_experiments: int,
    results: list[ExperimentResult],
) -> None:
    print()
    print("Experiment Summary")
    print("==================")

    print(
        f"Configured experiments: "
        f"{total_experiments}"
    )

    print(
        f"Completed experiments: "
        f"{completed_experiments}"
    )

    if not results:
        print(
            "No completed experiments."
        )
        return

    average_score = sum(
        result.score
        for result in results
    ) / len(results)

    total_duration = sum(
        result.duration_seconds
        for result in results
    )

    best_result = get_best_result(
        results
    )

    fastest_result = get_fastest_result(
        results
    )

    slowest_result = get_slowest_result(
        results
    )

    print(
        f"Average score: "
        f"{average_score:.6f}"
    )

    print(
        f"Total runtime: "
        f"{total_duration:.6f} seconds"
    )

    if best_result is not None:
        print(
            f"Best score: "
            f"{best_result.name} "
            f"({best_result.score:.6f})"
        )

    if fastest_result is not None:
        print(
            f"Fastest experiment: "
            f"{fastest_result.name} "
            f"("
            f"{fastest_result.duration_seconds:.6f}s"
            f")"
        )

    if slowest_result is not None:
        print(
            f"Slowest experiment: "
            f"{slowest_result.name} "
            f"("
            f"{slowest_result.duration_seconds:.6f}s"
            f")"
        )