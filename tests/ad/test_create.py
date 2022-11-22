import pytest


@pytest.mark.django_db
def test_create(client, user, category, access_token):

    data = {
        "name": "nukaktams",
        "author": user.pk,
        "category": category.pk,
        "price": 3200,
        "description": "desc",
        "is_published": False
    }

    expected_data = {
        "id": 1,
        "name": "nukaktams",
        "author": 1,
        "category": 1,
        "price": 3200,
        "image": None,
        "description": "desc",
        "is_published": False
    }

    response = client.post('/ad/', data, content_type='application/json', HTTP_AUTHORIZATION=f"Bearer {access_token}")

    assert response.status_code == 201
    assert response.data == expected_data
