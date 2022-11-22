import pytest

from tests.factories import AdFactory


@pytest.mark.django_db
def test_select_create(client, user, ad, access_token):
    ads = AdFactory.create_batch(5)
    response = client.post('/selection/',
                           {"name": "test_name", "owner": user.pk,
                            "items": [ad.pk for ad in ads]},
                           content_type='application/json',
                           HTTP_AUTHORIZATION=f"Bearer {access_token}"
                           )

    assert response.status_code == 201
    assert response.data == {"id": 1, "name": "test_name", "owner": user.pk, "items": [ad.pk for ad in ads]}
