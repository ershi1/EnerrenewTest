# !/usr/bin python3
# encoding: utf-8 -*-
# @file   : /tests/testcase_example.py

import allure
import pytest
from socks import method
from src.api.client.http_client import HttpRequest
from src.core.utils.data_utils import load_yaml

BASE_URL = "http://192.168.3.54:20238"

test_data = load_yaml('data/statistics_test_data.yaml')

'''客户端实例，加载base_url和token'''
@pytest.fixture
def api_client():
    client = HttpRequest(BASE_URL)
    client.load_token("tests/data/config_token.json")
    return client

@allure.step("Send {method} request to{endpoint}")
def send_request(api_client, endpoint, params=None, headers=None, json=None):
    if method == 'GET':
        return api_client.get(endpoint, params=params, headers=headers)
    elif method == 'post':
        return api_client.post(endpoint, json=json, headers=headers)
    elif method == 'PUT':
        return api_client.put(endpoint, json=json, headers=headers)
    else:
        raise ValueError(f"没有配置的方法：{method}")

@pytest.mark.parametrize("test_case", test_data)
@allure.description("Test API endpoint with different test cases")
def test_api_endpoint(api_client, test_case):
    endpoint = test_case["endpoint"]
    method = test_case["method"]
    params = test_case.get("params", None)
    headers = test_case.get("headers", None)
    json_data = test_case.get("json", None)
    expected_status = test_case["expected_status"]

    with allure.step(f"Testing endpoint: {endpoint}"):
        response = send_request(api_client, method, endpoint, params=params, headers=headers, json=json_data)

    # 将响应内容附加到报告中
    allure.attach(response.text, name="Response Body", attachment_type=allure.attachment_type.TEXT)

    assert response.status_code == expected_status, f"Expected status {expected_status}, but got {response.status_code}"
