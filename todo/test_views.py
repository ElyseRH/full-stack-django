from django.test import TestCase
from .models import Item

class TestViews(TestCase):

    def test_get_todo_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')
    
    def test_get_edit_item(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/edit/{item.id}') # item id works here because of import and item created just above
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')
    
    def test_can_add_item(self):
        response = self.client.post('/add', {'name': 'Test Add Item'})
        self.assertRedirects(response, '/')


    def test_can_delete_item(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')
        existing_items = Item.objects.filter(id=item.id) # check if items exists by trying to retrieve it
        self.assertEqual(len(existing_items), 0) # test will pass if list is empty

    def test_can_toggle_item(self):
        item = Item.objects.create(name='Test Todo Item', done=True)
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)

    def test_can_edit_item(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.post(f'/edit/{item.id}', {'name', 'Updated Name'})
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertEqual(updated_item.done, 'Updated Name')