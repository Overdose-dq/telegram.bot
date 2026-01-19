from functools import wraps
import logging


def async_log_function_call(func):
    """Decorator for logging async function calls"""
    @wraps(func)
    async def wrapper(*args, **kwargs):
        logger = logging.getLogger(__name__)

        try:
            username = args[0].chat.username
        except (IndexError, AttributeError):
            username = "unknown"

        logger.info(f"{username} call '{func.__name__}'")
        return await func(*args, **kwargs)

    return wrapper
