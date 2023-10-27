from unittest.mock import patch
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class UserViewSetTests(APITestCase):
    @patch('user.views.post')
    def test_create_user_with_valid_data(self, mock_post):
        url = reverse('user-list')
        data = {
            "email": "test@example.com",
            "date_of_birth": "2000-01-01",
            "date_of_creation": "2023-10-26",
            "username": "testuser"
        }

        # Simula una respuesta exitosa de la API
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"message": "Registro de autenticación exitoso"}

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('email' in response.data)

    @patch('user.views.post')
    def test_create_user_with_invalid_data(self, mock_post):
        url = reverse('user-list')
        data = {
            "email": "invalid_email",  # Email inválido
            "date_of_birth": "invalid_date",  # Fecha de nacimiento inválida
            "date_of_creation": "invalid_date",  # Fecha de creación inválida
            "username": "short"  # Nombre de usuario muy corto
        }
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"message": "Registro de autenticación exitoso"}

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)






