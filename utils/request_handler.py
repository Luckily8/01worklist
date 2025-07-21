import requests
from utils.logger import get_logger

logger = get_logger()

class RequestHandler:
    def __init__(self, base_url, timeout=10):
        self.base_url = base_url
        self.timeout = timeout

    def send_request(self, method, endpoint, params=None, data=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"Sending {method} request to {url} with data: {data}")
        try:
            response = requests.request(
                method=method,
                url=url,
                params=params,
                json=data,
                headers=headers,
                timeout=self.timeout
            )
            logger.info(f"Response: {response.status_code}, {response.text}")
            return response
        except requests.RequestException as e:
            logger.error(f"Request failed: {e}")
            raise