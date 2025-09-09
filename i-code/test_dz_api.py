import pytest
import requests

'''
ДЗ2* 
Взять ответ с GET /users с сайта https://jsonplaceholder.typicode.com/
Вывести следующий текст:
"Всем привет, меня зовут name, я живу по улице street, в городе city,
если вы хотите связаться со мной пишите мне на email,
также я доступен по номеру phone, я работаю в компании company_name,
и мы занимаемся catchPrase, это в случае если вы заинтересованы bs"
'''

def test_create_post():

    user_id = int(input("Введите id: "))
    url = "https://jsonplaceholder.typicode.com/users"


    response = requests.get(f'{url}/{user_id}')
    assert response.status_code == 200
    data = response.json()
    # print(data)
    var = (f"Всем привет, меня зовут {data['name']}, я живу по улице {data['address']['street']}, "
       f"в городе {data['address']['city']}, если вы хотите связаться со мной пишите мне на {data['email']}, "
       f"также я доступен по номеру {data['phone']}, я работаю в компании {data['company']['name']}, "
       f"и мы занимаемся {data['company']['catchPhrase']}, это в случае если вы заинтересованы {data['company']['bs']}")
    print(var)

# 2й вариант как можно написать
def test_create_post2():
    user_id = int(input("Введите id: "))
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(f'{url}/{user_id}')
    assert response.status_code == 200

    data = response.json()

    name = data['name']
    street = data['address']['street']
    city = data['address']['city']
    email = data['email']
    phone = data['phone']
    company_name = data['company']['name']
    catch_phrase = data['company']['catchPhrase']
    company_bs = data['company']['bs']

    # print(data)
    var = (f"Всем привет, меня зовут {name}, я живу по улице {street}, "
       f"в городе {city}, если вы хотите связаться со мной пишите мне на {email}, "
       f"также я доступен по номеру {phone}, я работаю в компании {company_name}, "
       f"и мы занимаемся {catch_phrase}, это в случае если вы заинтересованы {company_bs}")
    print(var)


'''
ДЗ: Обработать ошибку - если не приходит формат json (проверить приходит json или нет 
и дальше в зависимости от результатов провести следующие тесты)

ВНИМАНИЕ: код содержит ошибку, ее нужно будет пофиксить, 
при этом решение должно быть универсальным при любом источнике данных
'''


def test_json_structure():
    global data_post
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    try:
        data_post = response.json()
        print(response.headers["Content-Type"])
    except ValueError:
        pytest.fail("Ответ не в формате JSON")

    # Дополнительные проверки на структуру
    assert isinstance(data_post, dict), "Ожидался словарь (JSON-объект)"

    required_keys = ["id", "title", "body"]
    for key in required_keys:
        assert key in data_post, f"Ключ '{key}' отсутствует в ответе"

    assert isinstance(data_post["title"], str), "'title' должен быть строкой"
    assert isinstance(data_post["body"], str), "'body' должен быть строкой"
    assert isinstance(data_post["id"], int), "'id' должен быть целым числом"

