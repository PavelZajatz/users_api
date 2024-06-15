import pytest

from infrastructure.api_methods.users import Users


@pytest.fixture()
def purge_data():
    Users().reset_user_data()


@pytest.fixture()
def create_user():
    response = Users().create_user()
    yield response
