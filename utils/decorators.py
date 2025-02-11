import functools
from utils.logger import logger

def log_request_response(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info("=" * 50)
        logger.info("Making API Request:")

        # 检查并记录 URL（args[1]）
        if len(args) > 1:
            logger.info(f"URL: {args[1]}")
        else:
            logger.info("URL: 未提供")

        # 检查并记录 Method（args[2]）
        if len(args) > 2:
            logger.info(f"Method: {args[2]}")
        else:
            logger.info("Method: 未提供")

        logger.info(f"Params: {kwargs.get('params')}")
        logger.info(f"Headers: {kwargs.get('headers')}")
        logger.info(f"Request Body: {kwargs.get('json')}")

        response = func(*args, **kwargs)

        logger.info("API Response:")
        logger.info(f"Status Code: {response.status_code}")
        logger.info(f"Response Body: {response.text}")
        logger.info("=" * 50)

        return response
    return wrapper