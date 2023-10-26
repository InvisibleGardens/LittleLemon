from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):

        Menu.objects.create(name="Item 1", description="Description 1")
        Menu.objects.create(name="Item 2", description="Description 2")
        Menu.objects.create(name="Item 3", description="Description 3")

    def test_getall(self):
        response = self.client.get('/your-api-endpoint/') 

        self.assertEqual(response.status_code, 200)

        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        self.assertEqual(response.data, serializer.data)
