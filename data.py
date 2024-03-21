import random


class Data:

    URL = 'http://qa-scooter.praktikum-services.ru'

    number = random.randint(11, 99)

    CREATE_COURIER = {
        "login": f"ohhOxana{number}",
        "password": "12345",
        "firstName": f"Oxana{number}"
    }

    CREATE_COURIER_DUPLICATE = {
        "login": "ohhOxana",
        "password": "12345",
        "firstName": "Oxana"
    }

    CC_RESPONSE_POSITIVE = {'ok': True}
    CC_RESPONSE_MANDATORY = {"message": "Недостаточно данных для создания учетной записи"}
    CC_RESPONSE_DUPLICATE = {"message": "Этот логин уже используется. Попробуйте другой."}

    LC_RESPONSE_MANDATORY = {"message": "Недостаточно данных для входа"}
    LC_RESPONSE_INCORRECT_DATA = {"message": "Учетная запись не найдена"}

    INCORRECT_LOGIN_DATA = {
        "login": "ohhOxanaOh",
        "password": "12345"
    }
