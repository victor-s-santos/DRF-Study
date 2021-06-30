import pytest
from django.urls import reverse
path_list_401 = [
    ('cursos', 401),
]

path_list_201 = [
    ('cursos', 201),
]

class Test_unauthenticated_post_request:
    @pytest.mark.django_db
    @pytest.mark.parametrize('path, status_code', path_list_401)
    def test_post_cursos(self, api_client, path, status_code):
        """Must return status_code 401"""
        url = reverse(path)
        novo_curso = {
            "titulo": "Pytest Django",
            "url": "https://www.youtube.com/pytest-django"
        }
        assert api_client.post(url, novo_curso).status_code == status_code

class Test_authenticated_post_request:
    @pytest.mark.django_db
    @pytest.mark.parametrize('path, status_code', path_list_201)
    def test_post_cursos(self, api_client_with_credentials, path, status_code):
        """Must return status_code 201"""
        url = reverse(path)
        novo_curso = {
            "titulo": "Pytest Django",
            "url": "https://www.youtube.com/pytest-django"
        }
        assert api_client_with_credentials.post(url, novo_curso).status_code == 201

