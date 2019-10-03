from django.urls import path


from users.views.users import UserCreateView
from users.views.user_auth import UserLoginView, UserLogoutView

urlpatterns = [
    # rest api urls
    path('create', UserCreateView.as_view()),
    # path('update', UserUpdateView.as_view()),
    path('login', UserLoginView.as_view()),


    # path('social/login', UserSocialLoginView.as_view()),
    path('logout', UserLogoutView.as_view()),
    # path('activation', UserActivationView.as_view()),
    # path('resend-activation', UserResendActivationView.as_view()),
    # path('reset-password', UserResetPasswordView.as_view()),
    # path('forget-password', UserForgetPasswordView.as_view()),
    # path('recover-password', UserRecoverPasswordView.as_view()),
    # path('data', UserDataView.as_view()),
    # path('list', UserListView.as_view()),
    # path('<user_slug>/book/list', UserBookListView.as_view()),
    # path('<user_slug>/chapter/list', UserChapterListView.as_view()),
    # path('<user_slug>', UserBySlugDataView.as_view()),
    #
    # path('<user_slug>/follow', UserFollowView.as_view()),
    # path('<user_slug>/unfollow', UserUnFollowView.as_view()),
    # path('<user_slug>/followers', UserFollowersView.as_view()),
    # path('<user_slug>/followings', UserFollowingUsersView.as_view()),
    # path('<user_slug>/following/books', UserFollowingBooksView.as_view()),
    # path('book/<book_slug>/follow', BookFollowView.as_view()),
    # path('book/<book_slug>/unfollow', BookUnFollowView.as_view()),
    # admin rest api urls
]
