import pytest
from src.api.services.order_api import OrderAPIClient

@pytest.fixture
def mock_payment_gateway():
    """模拟支付网关（仅限订单模块使用）"""
    # 实现模拟逻辑...
    return MockPaymentGateway()

@pytest.fixture
def order_client(api_client):
    """订单模块专用的接口客户端"""
    return OrderAPIClient(api_client)