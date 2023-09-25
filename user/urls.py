from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserRegistrationView, UserLoginView,UserProfileUpdateView,UserDeleteView
router=DefaultRouter()
router.register('register/', UserRegistrationView.as_view(), basename='user-registration')
router.register('profile/update/', UserProfileUpdateView.as_view(), name='profile-update')
router.register('login/', UserLoginView.as_view(), name='user-login')
router.register('profile/delete/',UserDeleteView.as_view(),name='user-delete')
urlpatterns = [
    path('',include(router.urls))
]
