from django.urls import path
from .views import UserRegistrationView, UserLoginView,UserProfileUpdateView,UserDeleteView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('profile/update/', UserProfileUpdateView.as_view(), name='profile-update'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('profile/delete/',UserDeleteView.as_view(),name='user-delete')
]
