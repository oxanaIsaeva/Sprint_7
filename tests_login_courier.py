import allure
import requests
import pytest
from data import Data


class TestLoginCourier:

    @classmethod
    def setup_class(cls):
        payload = Data.CREATE_COURIER
        requests.post(f'{Data.URL}/api/v1/courier', data=payload)

    @allure.title('Проверка успешной авторизации курьера')
    @allure.description('Запрос возвращает код ответа 200 и содержит "id" в ответе')
    def test_login_courier_positive(self):
        payload = Data.CREATE_COURIER
        response = requests.post(f'{Data.URL}/api/v1/courier/login', data=payload)
        format_response = response.json()

        assert response.status_code == 200 and 'id' in format_response.keys()

    @classmethod
    def teardown_class(cls):
        payload = Data.CREATE_COURIER
        response_login = requests.post(f'{Data.URL}/api/v1/courier/login', data=payload)
        response_id = response_login.json()["id"]
        requests.delete(f'{Data.URL}/api/v1/courier/{response_id}')

    @pytest.mark.parametrize(
        "login, password",
        [
            ['', '12345'],
            ['ohhOxana', '']
        ]
    )
    @allure.title('Проверка, что для авторизации нужно передать все обязательные поля')
    @allure.description('Запрос возвращает код ответа 400 и ответ: {"message": "Недостаточно данных для входа"}')
    @allure.issue('Тело ответа не соответствует спецификации')
    def test_login_courier_mandatory_fields(self, login, password):
        payload = {"login": login, "password": password}
        response = requests.post(f'{Data.URL}/api/v1/courier/login', data=payload)
        format_response = response.json()

        assert response.status_code == 400 and format_response == Data.LC_RESPONSE_MANDATORY

    @pytest.mark.parametrize(
        "login, password",
        [
            ['ohhOxana', '123'],
            ['ohhOxanaa', '12345']
        ]
    )
    @allure.title('Проверка, что система вернёт ошибку, если неправильно указать логин или пароль')
    @allure.description('Запрос возвращает код ответа 404 и ответ: {"message": "Учетная запись не найдена"}')
    @allure.issue('Тело ответа не соответствует спецификации')
    def test_login_courier_incorrect_data(self, login, password):
        payload = {"login": login, "password": password}
        response = requests.post(f'{Data.URL}/api/v1/courier/login', data=payload)
        format_response = response.json()

        assert response.status_code == 404 and format_response == Data.LC_RESPONSE_INCORRECT_DATA

    @allure.title('Проверка, что если авторизоваться под несуществующим пользователем, запрос возвращает ошибку')
    @allure.description('Запрос возвращает код ответа 404 и ответ: {"message": "Учетная запись не найдена"}')
    @allure.issue('Тело ответа не соответствует спецификации')
    def test_login_courier_without_password(self):
        payload = Data.INCORRECT_LOGIN_DATA
        response = requests.post(f'{Data.URL}/api/v1/courier/login', data=payload)
        format_response = response.json()

        assert response.status_code == 404 and format_response == Data.LC_RESPONSE_INCORRECT_DATA
