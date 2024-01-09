import pytest
from rest_framework.test import APIClient
from rest_framework import status
from users.models import User
from users.serializers import UserSerializer

def test_user_list(create_user):
    client = APIClient()
    response = client.get('/users/')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1

@pytest.mark.django_db
def test_create_user():
    client = APIClient()
    user_data = {
        'username': 'new_user',
        'password': 'new_password'
    }
    response = client.post('/users/', user_data)
    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.count() == 1
    assert response.data['username'] == user_data['username']

def test_user_detail(create_user):
    client = APIClient()
    user = create_user
    response = client.get(f'/users/{user.id}/')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['username'] == user.username
