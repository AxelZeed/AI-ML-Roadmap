import argparse

from src.paths import (
    CONFIG_DIR,
    EXPERIMENT_DIR,
)


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Run Axel AI Lab experiments."
        )
    )

    parser.add_argument(
        "--config",
        default=str(
            CONFIG_DIR / "experiments.yaml"
        ),
        help=(
            "Path to the experiment "
            "configuration file."
        ),
    )

    parser.add_argument(
        "--output",
        default=str(
            EXPERIMENT_DIR / "results.json"
        ),
        help=(
            "Path for the latest "
            "experiment results."
        ),
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help=(
            "Enable additional "
            "console information."
        ),
    )

    return parser.parse_args()