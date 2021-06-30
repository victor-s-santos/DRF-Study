import pytest
from django.urls import reverse


path_list_401 = [
    ('/api/v2/cursos/', 401),
]

path_list_201 = [
    #erro neste teste, retorna 403
    ('/api/v2/cursos/', 201),
]

class Test_unauthenticated_post_request:
    @pytest.mark.django_db
    @pytest.mark.parametrize('path, status_code', path_list_401)
    def test_post_cursos_unauthenticated(self, api_client, path, status_code):
        """Must return status_code 401"""
        novo_curso = {
            "titulo": "Pytest Django",
            "url": "https://www.youtube.com/pytest-django"
        }
        assert api_client.post(path, novo_curso).status_code == status_code

class Test_authenticated_post_request:
    @pytest.mark.django_db
    @pytest.mark.parametrize('path, status_code', path_list_201)
    def test_post_cursos_authenticated(self, api_client_with_credentials, path, status_code):
        """Must return status_code 201"""
        novo_curso = {
            "titulo": "Pytest Django2",
            "url": "https://www.youtube.com/pytest-django2"
        }
        assert api_client_with_credentials.post(path, novo_curso).status_code == status_code

#hard code way
@pytest.mark.django_db
def test_get_cursos_authenticated(api_client, get_or_create_token):
    """Must return status_code 200"""
    url = '/api/v2/cursos/'
    token = get_or_create_token
    api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    assert api_client.get(url).status_code == 200

@pytest.mark.django_db
def test_get_cursos_authenticated_other_fixture(api_client_with_credentials):
    url = '/api/v2/cursos/'
    assert api_client_with_credentials.get(url).status_code == 200
