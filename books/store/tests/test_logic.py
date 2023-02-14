from django.test import TestCase

from store.logic import operations


class LogicTestCase(TestCase):
    def test_plus(self):
        result = operations(6, 13, '+')
        self.assertEqual(19, result)
    
    def test_minus(self):
        result = operations(10, 8, '-')
        self.assertEqual(2, result)
    
    def test_product(self):
        result = operations(10, 8, '*')
        self.assertEqual(80, result)