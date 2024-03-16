import allure
import requests
import pytest
from data import Data



class TestCreateCourier:

    @allure.title('Проверка успешного создания курьера')
    @allure.description('Запрос возвращает код ответа 201 и ответ: {"ok":true}')
    def test_create_courier_positive(self):
        payload = Data.CREATE_COURIER
        response = requests.post('http://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        r = response.json()

        assert response.status_code == 201 and r == Data.CC_RESPONSE_POSITIVE

    @classmethod
    def teardown_class(cls):
        payload = Data.CREATE_COURIER
        response_login = requests.post('http://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        r_log = response_login.json()["id"]
        requests.delete(f'http://qa-scooter.praktikum-services.ru/api/v1/courier/{r_log}')

    @allure.title('Проверка, что нельзя создать двух одинаковых курьеров')
    @allure.description('Запрос возвращает код ответа 209 и ответ: {"message": "Этот логин уже используется. '
                        'Попробуйте другой."}')
    @allure.issue('Тело ответа не соответствует спецификации')
    def test_create_two_same_courier(self):
        payload = Data.CREATE_COURIER
        requests.post('http://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        response = requests.post('http://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        r = response.json()

        assert response.status_code == 409 and r == Data.CC_RESPONSE_DUPLICATE

    @classmethod
    def teardown_class(cls):
        payload = Data.CREATE_COURIER
        response_login = requests.post('http://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        r_log = response_login.json()["id"]
        requests.delete(f'http://qa-scooter.praktikum-services.ru/api/v1/courier/{r_log}')

    @pytest.mark.parametrize(
        "login, password, firstname",
        [
            ['', '12345', 'Oxana'],
            ['ohhOxana', '', 'Oxana']
        ]
    )
    @allure.title('Проверка, что чтобы создать курьера, нужно передать в ручку все обязательные поля')
    @allure.description('Запрос возвращает код ответа 400 и ответ: {"message": "Недостаточно данных для создания '
                        'учетной записи"}')
    @allure.issue('Тело ответа не соответствует спецификации')
    def test_create_courier_mandatory_fields(self, login, password, firstname):
        payload = {"login": login, "password": password, "firstName": firstname}
        response = requests.post('http://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        r = response.json()

        assert response.status_code == 400 and r == Data.CC_RESPONSE_MANDATORY

    @allure.title('Проверка, что если создать пользователя с логином, который уже есть, возвращается ошибка')
    @allure.description('Запрос возвращает код ответа 409 и ответ: {"message": "Этот логин уже используется. '
                        'Попробуйте другой."}')
    @allure.issue('Тело ответа не соответствует спецификации')
    def test_create_courier_duplicate_login(self):
        payload = Data.CREATE_COURIER_DUPLICATE
        response = requests.post('http://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        r = response.json()

        assert response.status_code == 409 and r == Data.CC_RESPONSE_DUPLICATE
