import pytest
from infrastructure.api_methods.users import Users
from infrastructure.helpers.help_methods import FileMethods
from infrastructure.helpers.schema_validate import ValidateResponse


class TestSavedSearches:

    def test_create_user(self, create_user):
        schema = FileMethods().get_json_file("/infrastructure/data/response_schema/create_user_schema.json")
        response = create_user
        ValidateResponse().validate_response(response, schema)

    def test_update_user(self, create_user):
        schema = FileMethods().get_json_file("/infrastructure/data/response_schema/update_user_schema.json")
        response = create_user
        ValidateResponse().validate_response(response, schema)

    def test_get_all_users(self, purge_data, create_user):
        response = Users().get_users()

    def test_get_user(self, create_user):
        schema = FileMethods().get_json_file("/infrastructure/data/response_schema/get_user_schema.json")
        user_id = create_user.json()["id"]
        response = Users().get_users(user_id)
        print(response.json())
        ValidateResponse().validate_response(response, schema)
