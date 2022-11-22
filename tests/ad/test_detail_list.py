import pytest

from ads.serializers import AdDetailSerializer


@pytest.mark.django_db
def test_detail_ad(client, ad, access_token):
    response = client.get(f"/ad/{ad.pk}/", content_type='application/json',
                          HTTP_AUTHORIZATION=f"Bearer {access_token}")

    assert response.status_code == 200
    assert response.data == AdDetailSerializer(ad).data
