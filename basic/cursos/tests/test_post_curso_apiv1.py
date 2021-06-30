import pytest

@pytest.mark.django_db
def test_post_curso_authenticated(api_client_with_credentials):
    """Must return status code 201"""
    url = '/api/v1/cursos/'
    novo_curso = {
        "titulo": "Pytest Django",
        "url": "https://www.youtube.com/pytest-django"
    }
    assert api_client_with_credentials.post(url, novo_curso).status_code == 201

@pytest.mark.django_db
def test_post_curso_unauthenticated(api_client):
    """Must return status code 401"""
    url = '/api/v1/cursos/'
    novo_curso = {
        "titulo": "Pytest Django",
        "url": "https://www.youtube.com/pytest-django"
    }
    assert api_client.post(url, novo_curso).status_code == 401
