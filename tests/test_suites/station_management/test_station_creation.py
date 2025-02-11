import pytest
from src.api.services.user_api import UserAPIClient


class TestUserCreation:
    @pytest.mark.parametrize("test_case", ["valid_user", "invalid_user"])
    def test_create_user(self, test_case, user_test_data):
        """测试用户创建场景"""
        data = user_test_data[test_case]
        response = UserAPIClient().create_user(data)

        if test_case == "valid_user":
            assert response.status_code == 201
            assert "user_id" in response.json()
        else:
            assert response.status_code == 400
            assert "error" in response.json()