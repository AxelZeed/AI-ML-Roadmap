from src.models import ExperimentResult


def get_best_result(
    results: list[ExperimentResult],
) -> ExperimentResult | None:
    if not results:
        return None

    return max(
        results,
        key=lambda result: result.score,
    )


def get_fastest_result(
    results: list[ExperimentResult],
) -> ExperimentResult | None:
    if not results:
        return None

    return min(
        results,
        key=lambda result: (
            result.duration_seconds
        ),
    )


def get_slowest_result(
    results: list[ExperimentResult],
) -> ExperimentResult | None:
    if not results:
        return None

    return max(
        results,
        key=lambda result: (
            result.duration_seconds
        ),
    )