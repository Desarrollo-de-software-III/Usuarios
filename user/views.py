
from rest_framework import viewsets
from rest_framework.response import Response
from http import HTTPStatus
from requests import post
# import local data
from .serializers import UserSerializer
from .models import User

def createAuthAccount(data:dict):
   #""remplazar url por la del microservicio auth"
   #crea la cuenta de autenticacion
    response = post("http://127.0.0.1:8000/login/", json=data)
    return response.status_code == 200, response

# create a viewset
class UserViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = User.objects.all()

    # specify serializer to be used
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        createAuth, response = createAuthAccount(request.data)
        if not createAuth:
            return Response(response.json(), status=response.status_code, headers=response.headers)

        # hacer las validaciones
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=HTTPStatus.CREATED, headers=headers)
        
