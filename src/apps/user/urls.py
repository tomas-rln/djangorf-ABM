from django.urls import path 

from api.api import user_api_view

urlpatterns = [
    path('all/', user_api_view, name='all_users'),
]
