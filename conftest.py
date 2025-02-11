import pytest
from utils.send_request import RequestUtils

@pytest.fixture
def request_utils():
    return RequestUtils
