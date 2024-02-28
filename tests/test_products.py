from tests.conftest import client


def test_create_product():
    response = client.post(
        "http://127.0.0.1:8000/api/v1/products",
        json={
          "name": "стул",
          "description": "из Ikea",
          "price": 10000,
          "count": 100
        }
    )

    if response.status_code == 201:
        assert True

    else:
        print('Неправильная валидация данных при создании резюме.')
        assert False