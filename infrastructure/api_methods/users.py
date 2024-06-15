import requests

from infrastructure.data.payload.user_payload import user_payload
from infrastructure.helpers.help_methods import GenerateStringMethods
from settings import *


class Users:
    url = BASE_URL + "/users"

    def get_users(self, user_id=False, success_response=True):
        url = self.url + f"/{user_id}" if user_id else self.url
        response = requests.get(url=url)
        if success_response:
            assert response.ok, f"Returned response with status code: {response.status_code}"
        return response

    def create_user(self, success_response=True):
        payload = user_payload
        payload['firstName'] = GenerateStringMethods().generate_random_string(10)
        payload['lastName'] = GenerateStringMethods().generate_random_string(10)
        payload['email'] = GenerateStringMethods().generate_random_email(10)
        response = requests.post(url=self.url, json=payload)
        if success_response:
            assert response.ok, f"Returned response with status code: {response.status_code}"
        return response

    def update_user(self, user_id, payload, success_response=True):
        payload['id'] = user_id
        response = requests.put(url=self.url + f"/{user_id}", json=payload)
        if success_response:
            assert response.ok, f"Returned response with status code: {response.status_code}"
        return response

    def reset_user_data(self):
        url = self.url + "/reset"
        response = requests.post(url=url)
        assert response.ok, f"Returned response with status code: {response.status_code}"
