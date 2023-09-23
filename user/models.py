from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password
# class myuser(models.Model):
#     username=models.CharField(max_length=35,unique=True)
#     password=models.CharField(max_length=35)
#     email = models.EmailField(unique=True)
#     mobile_number = models.CharField(max_length=15, blank=True, null=True)
#     image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_anonymous=False
#     is_authenticated=True
#     REQUIRED_FIELDS=[]
#     USERNAME_FIELD='username'
#     def get_by_natural_key(self, username):
#         return self.get(username=username)
#     def save(self,**kwargs):
#         self.password=make_password(self.password,'some_salt')
#         super().save(**kwargs)

#     def __str__(self):
#         return str(self.username)




class myuserManager(BaseUserManager):
    def create_user(self, username , password=None, **extra_fields):
        if not username:
            raise ValueError('The username must be set')
        user = self.model(username=username, password=password,**extra_fields)
        user.save()
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)

class myuser(AbstractBaseUser, PermissionsMixin):
    username=models.CharField(max_length=35,unique=True)
    password=models.CharField(max_length=35)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = myuserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def save(self,**kwargs):
        self.password=make_password(self.password,'some_salt')
        super().save(**kwargs)

    def __str__(self):
        return str(self.username)
