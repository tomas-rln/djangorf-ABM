from django.urls import path 

from api.api import UserApiView

urlpatterns = [
    path('all/', UserApiView.as_view(), name='all_users'),
]
