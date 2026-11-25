import allure
import requests

from urls import BASE_URL, USER_URL


class UserMethods:

    def __init__(self):
        self.headers = None
        self.url = f'{BASE_URL}{USER_URL}'

    @allure.step("Создать пользователя")
    def create_user(self, payload):
        response = requests.post(f'{self.url}register', data=payload)
        bearer_token = response.json().get("accessToken")
        if self.headers is None:
            self.headers = {'Authorization': f'{bearer_token}'}
        return response.status_code, response.text

    @allure.step("Удалить пользователя")
    def delete_user(self):
        if self.headers == {'Authorization': 'None'}:
            return None
        response = requests.delete(f'{self.url}user', headers=self.headers)
        return response.status_code, response.text
