from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Product

class ProductApiTestCase(APITestCase):

    def setUp(self):

        self.product = Product.objects.create(
            name = 'Laptop',
            description = 'Laptop gaming',
            price = 1200.00
        )

        #Urls de los endpoints o servicios
        self.list_url = reverse('lista_productos')
        self.store_url = reverse('guardar_producto')
        self.detail_url = lambda pk : reverse('ver_actualizar_borrar_productos', args=[pk])

        #validacion
        self.valid_payload = {
            'name' : 'Teclado',
            'description' : 'Teclado mecánico',
            'price' : '200.00'
        }

    def test_list_products(self):
        reponse = self.client.get(self.list_url)
        self.assertEqual(reponse.status_code, status.HTTP_200_OK)
        self.assertIsInstance(reponse.data, list)

    def test_create_product(self):
        response = self.client.post(self.store_url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], self.valid_payload['name'])

    def test_get_product_detail(self):
        response = self.client.get(self.detail_url(self.product.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.product.name)



