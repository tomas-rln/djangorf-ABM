from rest_framework.response import Response
from rest_framework import APIView 
from api.serializers import UserSerializer
from apps.user.models import User

class UserApiView(APIView):
    def get_all(self, request): 
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return Response(users_serializer.data)