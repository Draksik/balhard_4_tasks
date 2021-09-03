"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
На сервере хранятся данные пользователя. Пользователь решил очистить список своих
номеров.

Написать функцию clear_list, которая будет очищать переданный список.

ПРИМЕРЫ
--------------------------------------------------------------------------------
clear_list([1, 2, 3]) -> []
"""
user_data = {
    "first name": "Ivan",
    "last name": "Ivanov",
    "phones": [
        "+333221112266",
        "+333555879845"
    ]
}


def clear_list(collection: list) -> list:
    """Очищает переданный список

    :param collection: список для очищения
    :return: очищенный список
    """
    list = user_data("phones")
    list.clear()
    return collection


if __name__ == '__main__':
    print("Очищаем список номеров телефонов...")
    result = clear_list(user_data["phones"])
    print("Успешно очищено!" if not result and result is user_data["phones"] else "Ошибка...")
