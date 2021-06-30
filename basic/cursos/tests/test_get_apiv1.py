import pytest
from django.urls import reverse


path_list_200 = [
    ('cursos', 200),
    ('avaliacoes', 200)
]

class Test_get_request:
    @pytest.mark.django_db
    @pytest.mark.parametrize('path, status_code', path_list_200)
    def test_get_cursos(self, api_client, path, status_code):
        """Must return status_code 200"""
        url = reverse(path)
        assert api_client.get(url).status_code == status_code
