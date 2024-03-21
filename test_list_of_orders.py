import allure
import requests
from data import Data


class TestListOfOrders:

    @allure.title('Проверка получения списка заказов')
    @allure.description('Запрос возвращает код ответа 200 и содержит "orders" в ответе')
    def test_list_of_orders(self):
        response = requests.get(f'{Data.URL}/api/v1/orders')
        format_response = response.json()

        assert response.status_code == 200 and 'orders' in format_response.keys()
