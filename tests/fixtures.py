import pytest


@pytest.fixture
@pytest.mark.django_db
def access_token(client, django_user_model):
    data = {
        "username": "testuser",
        "password": "testpass",
        "role": "admin"
    }

    django_user_model.objects.create_user(username=data['username'], password=data["password"], role=data['role'])
    response = client.post("/user/token/", {"username": data['username'], "password": data['password']},
                           content_type="application/json")

    return response.data['access']
