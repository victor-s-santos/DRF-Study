import pytest
from django.urls import reverse


@pytest.fixture
def api_client():
   from rest_framework.test import APIClient
   return APIClient()

@pytest.mark.django_db
def test_get_cursos_unauthorized(api_client):
    """Must return status_code 401"""
    url = '/api/v2/cursos/'
    assert api_client.get(url).status_code == 401

