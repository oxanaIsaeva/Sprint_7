import allure
import requests
import pytest
from data import Data


class TestCreateOrder:

    @pytest.mark.parametrize(
        "color",
        [
            ["BLACK"],
            ["GREY"],
            ["BLACK", "GREY"],
            []
        ]
    )
    @allure.title('Проверка успешного создания заказа с разными комбинациями параметра color')
    @allure.description('Запрос возвращает код ответа 201 и содержит "track" в ответе')
    @allure.issue('Нельзя создать заказ с одним значением параметра color через pycharm')
    def test_create_order(self, color):
        payload = {
            "firstName": "Ivan",
            "lastName": "Ivanov",
            "address": "Moskovsky, 155",
            "metroStation": 3,
            "phone": "+7 800 555 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "test test",
            "color": color
        }
        response = requests.post(f'{Data.URL}/api/v1/orders', data=payload)
        format_response = response.json()

        assert response.status_code == 201 and 'track' in format_response.keys()
