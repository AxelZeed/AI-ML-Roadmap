from src.models import ExperimentResult

def print_summary(
    total_experiments: int,
    completed_experiments: int,
    results: list[ExperimentResult],
) -> None:

    print()
    print("Experiment Summary")
    print("==================")
    print(f"Total experiments: {total_experiments}")
    print(f"Completed experiments: {completed_experiments}")

    if results:
        total_score = sum(
            result.score
            for result in results
        )
        average_score = total_score / len(results)

        print(f"Average score: {average_score}")
    else:
        print("Average score: No completed experiments")