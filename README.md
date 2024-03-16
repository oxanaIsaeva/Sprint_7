test_create_courier.py
TestCreateCourier
1. test_create_courier_positive - Проверка успешного создания курьера
2. test_create_two_same_courier - Проверка, что нельзя создать двух одинаковых курьеров
3. test_create_courier_mandatory_fields - Проверка, что чтобы создать курьера, нужно передать в ручку все обязательные поля
4. test_create_courier_duplicate_login - Проверка, что если создать пользователя с логином, который уже есть, возвращается ошибка

test_login_courier.py
TestLoginCourier
1. test_login_courier_positive - Проверка успешной авторизации курьера
2. test_login_courier_mandatory_fields - Проверка, что для авторизации нужно передать все обязательные поля
3. test_login_courier_incorrect_data - Проверка, что система вернёт ошибку, если неправильно указать логин или пароль
4. test_login_courier_without_password - Проверка, что если авторизоваться под несуществующим пользователем, запрос возвращает ошибку

test_create_order.py
TestCreateOrder
1. test_create_order - Проверка успешного создания заказа с разными комбинациями параметра color

test_lest_of_orders.py
TestListOfOrders
1. Проверка получения списка заказов# Sprint_7
