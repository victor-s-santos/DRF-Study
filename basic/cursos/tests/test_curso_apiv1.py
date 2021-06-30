import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_get_cursos(api_client):
    """Must return status_code 200"""
    url = reverse('cursos')
    assert api_client.get(url).status_code == 200

@pytest.mark.django_db
def test_get_avaliacoes(api_client):
    """Must return status_code 200"""
    url = reverse('avaliacoes')
    assert api_client.get(url).status_code == 200

