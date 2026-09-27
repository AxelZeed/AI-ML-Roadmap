import logging

import requests


BASE_URL = "https://jsonplaceholder.typicode.com"

logger = logging.getLogger("axel-ai-lab")


def get_post(
    post_id: int,
) -> dict[str, object] | None:
    try:
        response = requests.get(
            f"{BASE_URL}/posts/{post_id}",
            timeout=10,
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.Timeout:
        logger.error(
            "API request timed out for post %s",
            post_id,
        )

    except requests.exceptions.ConnectionError:
        logger.error(
            "Could not connect to API"
        )

    except requests.exceptions.HTTPError as error:
        logger.error(
            "HTTP error while fetching post %s: %s",
            post_id,
            error,
        )

    except requests.exceptions.JSONDecodeError:
        logger.error(
            "API returned invalid JSON"
        )

    return None

def get_posts_by_user(
    user_id: int,
) -> list[dict[str, object]]:
    try:
        response = requests.get(
            f"{BASE_URL}/posts",
            params={
                "userId": user_id,
            },
            timeout=10,
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as error:
        logger.error(
            "Could not fetch posts for user %s: %s",
            user_id,
            error,
        )

        return []

def create_post(
    title: str,
    body: str,
    user_id: int,
) -> dict[str, object] | None:
    payload = {
        "title": title,
        "body": body,
        "userId": user_id,
    }

    try:
        response = requests.post(
            f"{BASE_URL}/posts",
            json=payload,
            timeout=10,
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as error:
        logger.error(
            "Could not create post: %s",
            error,
        )

        return None