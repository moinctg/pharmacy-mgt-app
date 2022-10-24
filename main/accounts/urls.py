from django.urls import path, include
from .views import (
    CreateuserView, LoginView, UpdatePasswordView, MyView,
    UserActivitiesView, UsersView
)

from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)

router.register("create-user", CreateuserView, 'create user')
router.register("login", LoginView, 'login')
router.register("update-password", UpdatePasswordView, 'update password')
router.register("me", MyView, 'me')
router.register("activities-log", UserActivitiesView, 'activities log')
router.register("users", UsersView, 'users')

urlpatterns = [
    path("", include(router.urls))
]






# from django.urls import path
# # from accounts import views
# from accounts.views import SendPasswordResetEmailView, UserChangePasswordView, UserLoginView, UserProfileView, UserRegistrationView, UserPasswordResetView
# urlpatterns = [
#     path('register/', UserRegistrationView.as_view(),name="register"),
#     path('login/', UserLoginView.as_view(), name='login'),
#     path('profile/', UserProfileView.as_view(), name='profile'),
#     path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
#     path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
#     path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),



