import random
import string
from django.db.utils import IntegrityError, DataError
from usuarios.models import Usuario
from django.test import TestCase


class UsuarioTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.usuario1 = Usuario.objects.create(
            nome="test1", password="test1", email="test1@mail.com"
        )
        cls.usuario2 = Usuario.objects.create(
            nome="test2", password="test2", email="test2@mail.com"
        )

    def test_usuario_fields(self):
        self.usuario1.save()
        self.usuario2.save()

    def test_usuario_duplicated_email(self):
        with self.assertRaises(IntegrityError):
            self.usuario1.save()
            self.usuario2.email = "test1@mail.com"
            self.usuario2.save()

    def test_max_length_fields(self):
        with self.assertRaises(DataError):
            self.usuario1.nome = "".join(
                random.choice(string.ascii_letters + string.digits) for _ in range(256)
            )
            self.usuario1.email = "".join(
                random.choice(string.ascii_letters + string.digits) for _ in range(256)
            )
            self.usuario1.save()
