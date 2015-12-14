import factory
from .models import User


class UserFactory(factory.Factory):
    class Meta:
        model = User
    firstname = 'lin'
    lastname = 'l'
