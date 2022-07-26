from enum import auto
from django.test import TestCase
from .models import Auto
# Create your tests here.


class AutoTest(TestCase):
    
    def setUp(self):
        Auto.objects.create(marca="BMW", modelo= "Q3", año ="20172312241", precio = "50000")
    def test_auto_marca(self):
        auto = Auto.objects.get(modelo = "Q3")
        self.assertEqual(auto.marca, "BMW")
