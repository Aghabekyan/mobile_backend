from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
# from users.views.user import UserDetail
# from users.views.user_password import UserPasswordDetail
# from users.views.token import TokenDetail
# from users.views.sign_up import SignUpDetail
# from main.views.fcm_token import FCMTokenDetail

urlpatterns = [
    url(r'api/v1/users/', include(('users.urls', 'users'), namespace='users'))
]

# urlpatterns = [
#     path('api/v1/sign_up', SignUpDetail.as_view({'post': 'sign_up'})),
#     path('api/v1/token', TokenDetail.as_view({'post': 'token'})),
#     path('api/v1/token/refresh', TokenDetail.as_view({'post': 'refresh_token'})),
#
#
#
#
#     path('api/v1/users', UserDetail.as_view({'get': 'retrieve_all',
#                                                   'post': 'create'})),
#     path('api/v1/users/<slug:pk>', UserDetail.as_view({'get': 'retrieve',
#                                                             'put': 'update',
#                                                             'patch': 'partial_update',
#                                                             'delete': 'destroy'})),
#
#
#
#
#     path('api/v1/reset_password', UserPasswordDetail.as_view({'post': 'reset_password'})),
#     path('api/v1/change_password', UserPasswordDetail.as_view({'post': 'change_password'})),
#
#     path('api/v1/users/<slug:uid>/fcm', FCMTokenDetail.as_view({'post': 'create'})),
#     path('api/v1/users/<slug:uid>/fcm/<slug:token>', FCMTokenDetail.as_view({'delete': 'destroy'})),
# ]
