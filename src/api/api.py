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
        user_serializer = UserSerializer(data = request.data)
        if user_serializer.is_valid(): 
            user_serializer.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors)

@api_view(['GET','PUT'])
def user_detail_view(request, pk):
    if request.method == 'GET' and pk: 
        user = User.objects.filter(id = pk).first()
        user_serializer = UserSerializer(user) 
        return Response(user_serializer.data)