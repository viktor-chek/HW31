import pytest

from ads.serializers import AdSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def test_list_ad(client, access_token):
    ads = AdFactory.create_batch(5)

    response = client.get("/ad/", content_type='application/json', HTTP_AUTHORIZATION=f"Bearer {access_token}")

    assert response.status_code == 200
    assert response.data == {
        "count": 5,
        "next": None,
        "previous": None,
        "results": AdSerializer(ads, many=True).data
    }

