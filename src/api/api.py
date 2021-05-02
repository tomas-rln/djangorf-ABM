from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from api.serializers import UserSerializer
from apps.user.models import User

@api_view(['GET', 'POST'])
def user_api_view(request):
    if (request.method == 'GET'): 
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return Response(users_serializer.data)
    if (request.method == 'POST'): 
        print(request.data)