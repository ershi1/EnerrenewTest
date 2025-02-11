
class APIRequestException(Exception):
    """Custom exception for API failures"""
    def __init__(self, message, status_code=None):
        super().__init__(message)
        self.status_code = status_code

# 在请求封装层添加
try:
    response = requests.request(...)
except requests.exceptions.RequestException as e:
    raise APIRequestException(f"API请求失败: {str(e)}")
