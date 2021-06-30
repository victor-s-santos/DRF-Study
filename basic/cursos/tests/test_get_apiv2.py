import pytest
from django.urls import reverse


path_list_401 = [
    ('/api/v2/cursos/', 401)
]

path_list_200 = [
    ('/api/v2/cursos/', 200)
]

class Test_get_request:
    @pytest.mark.django_db
    @pytest.mark.parametrize('path, status_code', path_list_401)
    def test_get_cursos_unauthenticated(self, api_client, path, status_code):
        """Must return status_code 401"""
        assert api_client.get(path).status_code == status_code


    @pytest.mark.django_db
    @pytest.mark.parametrize('path, status_code', path_list_200)
    def test_get_cursos_authenticated(self, api_client_with_credentials, path, status_code):
        """Must return status_code 200"""
        assert api_client_with_credentials.get(path).status_code == status_code
