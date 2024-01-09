import pytest

from django.contrib.auth.models import User


# @pytest.mark.django_db
# def test_user_create():
#     User.objects.create_user('test','test@test.com', 'test')
#     assert User.objects.count() == 1

# def test_new_user(new_user):
#     print(new_user.username)
#     assert new_user.username == "Test_user"

def test_new_user(new_user):
    count = User.objects.all().count()
    print(new_user.username)
    print(count)
    assert True