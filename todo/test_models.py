from django.test import TestCase
from .models import Item


#testing to do items begin as false (not done)
class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        item = Item.objects.create(name='Test Todo Item')
        self.assertFalse(item.done)