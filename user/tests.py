from unittest.mock import patch
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class UserViewSetTests(APITestCase):
    @patch('your_module.post')
    def test_create_user_with_valid_data(self, mock_post):
        url = reverse('user-list')
        data = {
            "email": "test@example.com",
            "date_of_birth": "2000-01-01",
            "date_of_creation": "2023-10-26",
            "username": "testuser"
        }

        # Simula una respuesta exitosa de la API http://127.0.0.1:8000/login/
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"message": "Registro de autenticación exitoso"}

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('email' in response.data)
        # Agrega más aserciones según los campos que esperas en la respuesta.

    def test_create_user_with_invalid_data(self):
        url = reverse('user-list')
        data = {
            "email": "invalid_email",  # Email inválido
            "date_of_birth": "invalid_date",  # Fecha de nacimiento inválida
            "date_of_creation": "invalid_date",  # Fecha de creación inválida
            "username": "short"  # Nombre de usuario muy corto
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Agrega más aserciones según el tipo de errores esperados.

    def test_create_user_with_duplicate_email(self):
        # Crea un usuario con el mismo email
        User.objects.create_user(
            email="test@example.com",
            date_of_birth="2000-01-01",
            date_of_creation="2023-10-26",
            username="existinguser"
        )

        url = reverse('user-list')
        data = {
            "email": "test@example.com",
            "date_of_birth": "2000-01-01",
            "date_of_creation": "2023-10-26",
            "username": "testuser"
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Agrega aserciones según el tipo de error esperado.

    def test_create_user_with_valid_data_and_auth_error(self):
        # Simula un error en la creación de la cuenta de autenticación
        def mock_createAuthAccount(data):
            return False, Response({"error": "Error en la creación de la cuenta de autenticación"}, status=500)

        with unittest.mock.patch('your_module.createAuthAccount', new=mock_createAuthAccount):
            url = reverse('user-list')
            data = {
                "email": "test@example.com",
                "date_of_birth": "2000-01-01",
                "date_of_creation": "2023-10-26",
                "username": "testuser"
            }

            response = self.client.post(url, data, format='json')

            self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

