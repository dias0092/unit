import factory
from factory import django
from ..models import User

class UserFactory(django.DjangoModelFactory):
    class Meta:
        model = User

    name = factory.Faker('name')
    email = factory.Faker('email')
    is_active = factory.Faker('pybool')

