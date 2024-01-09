import factory
from faker import Faker
from users.models import User

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    id = factory.Faker('uuid4')
    username = factory.Faker('user_name')
    password = factory.Faker('password')
