import pytest

from app.users.models import User

pytestmark = pytest.mark.django_db


def test_user_get_absolute_url(user: User):
    assert user.get_absolute_url() == f"/users/{user.username}/"


def test_user_str(user: User):
    assert user.__str__() == f"{user.name}"
