import pytest
import uuid
from rest_framework.authtoken.models import Token

@pytest.fixture
def api_client():
   from rest_framework.test import APIClient
   return APIClient()

@pytest.fixture
def test_password():
   return 'strong-test-pass'

@pytest.fixture
def create_user(db, django_user_model, test_password):
   def make_user(**kwargs):
       kwargs['password'] = test_password
       if 'username' not in kwargs:
           kwargs['username'] = str(uuid.uuid4())
       return django_user_model.objects.create_user(**kwargs)
   return make_user

@pytest.fixture
def get_or_create_token(db, create_user):
    user = create_user()
    token, _ = Token.objects.get_or_create(user=user)
    return token

@pytest.fixture
def api_client_with_credentials(
   db, create_user, api_client
):
   user = create_user()
   api_client.force_authenticate(user=user)
   yield api_client
   api_client.force_authenticate(user=None)