from django.urls import path
from users import views

urlpatterns = [
    path('api/v1/users', views.UserDetail.as_view({'get': 'retrieve_all',
                                                   'post': 'create'})),
    path('api/v1/users/<int:pk>', views.UserDetail.as_view({'get': 'retrieve',
                                                            'put': 'update',
                                                            'patch': 'partial_update',
                                                            'delete': 'destroy'})),
]
