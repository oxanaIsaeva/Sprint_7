import allure
import requests


class TestListOfOrders:

    @allure.title('Проверка получения списка заказов')
    @allure.description('Запрос возвращает код ответа 200 и содержит "orders" в ответе')
    def test_list_of_orders(self):
        response = requests.get('http://qa-scooter.praktikum-services.ru/api/v1/orders')
        r = response.json()

        assert response.status_code == 200 and 'orders' in r.keys()