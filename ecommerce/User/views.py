from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import update_last_login
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import get_user_model


@api_view(['POST',])

@permission_classes((permissions.AllowAny, )) 
def registration_view(request):
    if request.method == 'POST':

        serializer = UserSerializer(data=request.data)
        
        data = {}
        if serializer.is_valid():

            account = serializer.save()

            data['response'] = "successfully registred a new user"
            data['email'] = account.email
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            print(token)
            data['token'] = token

        else:
            data = serializer.errors
        print('done!!!!!!!!!!')
        return Response(data)


class TokenAuthenticationView(ObtainAuthToken):
    """Implementation of ObtainAuthToken with last_login update"""
    
    def post(self, request):
        result = super(TokenAuthenticationView, self).post(request)
        currentUserModel = get_user_model()
        try:
            user = currentUserModel.objects.get(username=request.data['username'])
            update_last_login(None, user)
        except Exception as exc:
            return None
        return result