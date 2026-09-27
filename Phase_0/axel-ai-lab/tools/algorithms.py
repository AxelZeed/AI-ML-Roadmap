def binary_search(
    values: list[int],
    target: int,
) -> int | None:
    left = 0
    right = len(values) - 1

    while left <= right:
        middle = (left + right) // 2
        middle_value = values[middle]

        if middle_value == target:
            return middle

        if middle_value < target:
            left = middle + 1
        else:
            right = middle - 1

    return None

from collections import deque


def breadth_first_search(
    graph: dict[str, list[str]],
    start: str,
    target: str,
) -> bool:
    queue = deque([start])
    visited = {start}

    while queue:
        current = queue.popleft()

        if current == target:
            return True

        for neighbor in graph.get(
            current,
            [],
        ):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return False

def depth_first_search(
    graph: dict[str, list[str]],
    start: str,
    target: str,
) -> bool:
    stack = [start]
    visited = set()

    while stack:
        current = stack.pop()

        if current == target:
            return True

        if current in visited:
            continue

        visited.add(current)

        for neighbor in graph.get(
            current,
            [],
        ):
            if neighbor not in visited:
                stack.append(neighbor)

    return False