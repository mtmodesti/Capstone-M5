import json
from rest_framework.test import APITestCase
import ipdb
from django.utils import timezone
from usuarios.models import Usuario


class MedicoTestView(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        ...