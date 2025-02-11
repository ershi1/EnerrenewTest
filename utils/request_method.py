import json
import os.path
import requests
from utils.decorators import log_request_response

class HttpRequest:
    def __init__(self, base_url, token=None):
        self.base_url = base_url
        self.token = token

    #从配置文件获取token
    @log_request_response
    def load_token(self, file_path = "config_token.json"):
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                config = json.load(file)
                self.token = config.get("token")
                self.token_expiry = config.get("token_expiry")
        else:
            raise FileNotFoundError(f"token not found")

    #get请求
    @log_request_response
    def get(self, endpoint, params=None, headers=None, **kwargs):
        url = f"{self.base_url}{endpoint}"
        if headers is None:
            headers = {}
        if self.token:  # 如果存在 Token，自动附加到请求头
            headers["Authorization"] = f"Bearer {self.token}"
        response = requests.get(url, params=params, headers=headers)
        return response

    #处理post请求
    @log_request_response
    def post(self, endpoint, data=None, json=None, headers=None, **kwargs):
        url = f"{self.base_url}{endpoint}"
        if headers is None:
            headers = {}
        if self.token:  # 如果存在 Token，自动附加到请求头
            headers["Authorization"] = f"Bearer {self.token}"
        response = requests.post(url, data=data, json=json, headers=headers)
        return response

    #处理put请求
    @log_request_response
    def put(self, endpoint, data=None, json=None, headers=None, **kwargs):
        url = f"{self.base_url}{endpoint}"
        if headers is None:
            headers = {}
        if self.token:  # 如果存在 Token，自动附加到请求头
            headers["Authorization"] = f"Bearer {self.token}"
        response = requests.put(url, data=data, json=json, headers=headers)
        return response


    #处理delete请求
    @log_request_response
    def delete(self, endpoint, headers=None, **kwargs):
        url = f"{self.base_url}{endpoint}"
        if headers is None:
            headers = {}
        if self.token:  # 如果存在 Token，自动附加到请求头
            headers["Authorization"] = f"Bearer {self.token}"
        response = requests.delete(url, headers=headers)
        return response
