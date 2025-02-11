import requests

class RequestUtils:
    @staticmethod
    def send_request(method, url, headers=None, data=None):
        response = requests.request(method, url, headers=None, json=data)
        return response