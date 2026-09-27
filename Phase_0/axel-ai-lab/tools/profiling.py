import time
from collections.abc import Callable
from typing import Any


def time_function(
    function: Callable[..., Any],
) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()

        result = function(*args, **kwargs)

        end_time = time.perf_counter()
        duration = end_time - start_time

        print(
            f"{function.__name__} took "
            f"{duration:.6f} seconds"
        )

        return result

    return wrapper