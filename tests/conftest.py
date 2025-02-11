import pytest
from src.core.requests.client import RequestUtils

@pytest.fixture
def request_utils():
    return RequestUtils

import pytest
from src.core.database import DatabaseClient
from src.api.client.http_client import APIClient

@pytest.fixture(scope="session")
def db_connection():
    """全局数据库连接夹具"""
    db = DatabaseClient()
    db.connect()
    yield db
    db.close()

@pytest.fixture(scope="module")
def api_client():
    """接口客户端夹具"""
    return APIClient(base_url="https://api.example.com")

@pytest.fixture
def user_test_data(load_test_data):
    """加载用户测试数据"""
    return load_test_data("user_management/create_user.json")