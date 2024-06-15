import pytest
from infrastructure.api_methods.users import Users
from infrastructure.helpers.help_methods import FileMethods
from infrastructure.helpers.schema_validate import ValidateResponse


class TestUsers:

    def test_create_user(self, create_user):
        """Test to verify user creation"""
        schema = FileMethods().get_json_file("/infrastructure/data/response_schema/create_user_schema.json")
        response = create_user
        ValidateResponse().validate_response(response, schema)

    def test_update_user(self, create_user):
        """Test to verify successful user update"""
        schema = FileMethods().get_json_file("/infrastructure/data/response_schema/update_user_schema.json")
        user_id = create_user.json()["id"]
        payload = {'firstName': "UserUpdated"}
        response = Users().update_user(user_id, payload)
        ValidateResponse().validate_response(response, schema)

    def test_failed_update_user(self, create_user):
        """Test to verify unsuccessful user update"""
        user_id = create_user.json()["id"]
        payload = {'NewField': "UserUpdated"}
        response = Users().update_user(user_id, payload, success_response=False)
        assert response.status_code == 404, f"Status code 404 should be returned instead of {response.status_code}"

    def test_get_all_users(self, purge_data, create_user):
        """Test to verify retrieving all users list"""
        schema = FileMethods().get_json_file("/infrastructure/data/response_schema/get_user_schema.json")
        response = Users().get_users()
        ValidateResponse().validate_response(response, schema)


    def test_get_user(self, create_user):
        """Test to verify retrieving user by id"""
        schema = FileMethods().get_json_file("/infrastructure/data/response_schema/get_user_schema.json")
        user_id = create_user.json()["id"]
        response = Users().get_users(user_id)
        ValidateResponse().validate_response(response, schema)

    def test_get_unlisted_user(self, purge_data):
        """Test to verify retrieving user by non-existed id"""
        user_id = 1
        response = Users().get_users(user_id, success_response=False)
        assert response.status_code == 404, f"Status code 404 should be returned instead of {response.status_code}"

