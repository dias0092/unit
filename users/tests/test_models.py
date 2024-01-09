import pytest
from ..models import User

@pytest.mark.django_db
def test_user_create(user):
    assert User.objects.count() == 1

@pytest.mark.django_db
def test_user_read(user):
    fetched_user = User.objects.get(id = user.id)
    assert fetched_user == user

@pytest.mark.django_db
def test_user_update(user):
    user.name = 'newusername'
    user.save()
    assert User.objects.get(id=user.id).name == "newusername"

@pytest.mark.django_db
def test_user_delete(user):
    user_id = user.id
    user.delete()
    assert not User.objects.filter(id=user_id).exists()


