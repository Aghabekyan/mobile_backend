from django.urls import path
from users.views import user, user_password
from main.views import fcm_token

urlpatterns = [
    path('api/v1/users', user.UserDetail.as_view({'get': 'retrieve_all',
                                                  'post': 'create'})),
    path('api/v1/users/<slug:pk>', user.UserDetail.as_view({'get': 'retrieve',
                                                            'put': 'update',
                                                            'patch': 'partial_update',
                                                            'delete': 'destroy'})),

    path('api/v1/reset_password', user_password.UserPasswordDetail.as_view({'post': 'reset_password'})),
    path('api/v1/change_password', user_password.UserPasswordDetail.as_view({'post': 'change_password'})),

    path('api/v1/users/<slug:uid>/fcm', fcm_token.FCMTokenDetail.as_view({'post': 'create'})),
    path('api/v1/users/<slug:uid>/fcm/<slug:token>', fcm_token.FCMTokenDetail.as_view({'delete': 'destroy'})),
]
