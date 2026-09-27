from pathlib import Path

from src.cli import parse_arguments
from src.config import load_experiments
from src.environment import (
    get_api_key,
    get_environment_mode,
)
from src.experiment import run_experiment
from src.generators import (
    iter_runnable_experiments,
)
from src.logger import setup_logger
from src.paths import (
    EXPERIMENT_DIR,
    ensure_project_directories,
    get_run_directory,
)
from src.reporting import print_summary
from src.storage import (
    append_results_to_csv,
    save_results,
    save_run_result,
)


def main() -> None:
    ensure_project_directories()

    logger = setup_logger()

    logger.info(
        "Axel AI Lab started"
    )

    args = parse_arguments()

    config_path = Path(args.config)
    output_path = Path(args.output)

    history_path = (
        EXPERIMENT_DIR
        / "history.csv"
    )

    environment_mode = (
        get_environment_mode()
    )

    api_key = get_api_key()

    logger.info(
        "Environment mode: %s",
        environment_mode,
    )

    if api_key is None:
        logger.debug(
            "No API key configured"
        )
    else:
        logger.debug(
            "API key is configured"
        )

    if args.verbose:
        print()
        print("CLI Configuration")
        print("=================")
        print(
            f"Config: {config_path}"
        )
        print(
            f"Output: {output_path}"
        )
        print(
            f"History: {history_path}"
        )

    experiments = load_experiments(
        config_path
    )

    logger.info(
        "Loaded %s experiments",
        len(experiments),
    )

    print()
    print("Axel AI Lab")
    print("===========")

    results = []

    for experiment in (
        iter_runnable_experiments(
            experiments
        )
    ):
        print()

        result = run_experiment(
            experiment
        )

        results.append(result)

        run_directory = get_run_directory(
            result.run_id
        )

        run_result_file = save_run_result(
            result,
            run_directory,
        )

        logger.info(
            "Saved run result: %s",
            run_result_file,
        )

        logger.info(
            "Experiment completed: %s",
            experiment.name,
        )

    print_summary(
        len(experiments),
        len(results),
        results,
    )

    save_results(
        results,
        output_path,
    )

    append_results_to_csv(
        results,
        history_path,
    )

    logger.info(
        "Saved latest results to %s",
        output_path,
    )

    logger.info(
        "Appended history to %s",
        history_path,
    )

    logger.info(
        "Axel AI Lab finished"
    )


if __name__ == "__main__":
    main()