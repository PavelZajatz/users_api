import pytest

from infrastructure.api_methods.users import Users


@pytest.fixture()
def purge_data():
    """Fixture handles users data reset before test"""
    Users().reset_user_data()


@pytest.fixture()
def create_user():
    """Fixture handles new user creation before test and pass user data to test"""
    response = Users().create_user()
    yield response
