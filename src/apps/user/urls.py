from django.urls import path 

from api.api import user_api_view, user_detail_view

urlpatterns = [
    path('all/', user_api_view, name='all_users'),
    path('<int:pk>/', user_detail_view, name='user_detail')
]
