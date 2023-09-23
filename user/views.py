from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import myuser
from .serializers import myuserSerializer
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = myuserSerializer
    permission_classes = [permissions.AllowAny]



class UserProfileUpdateView(generics.UpdateAPIView):
    queryset = myuser.objects.all()
    serializer_class = myuserSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self):
        return myuser.objects.get(username=self.request.user.username)
    

class UserLoginView(APIView):
    permission_classes = [permissions.AllowAny]
    @csrf_exempt
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = myuser.objects.filter(username=username).first()
        print(user)
        if user is None:
            return Response({'detail': 'Invalid credentials'}, status=401)
        if not check_password(password,user.password):
            return Response({'detail': 'Invalid credentials'}, status=401)
        refresh = RefreshToken.for_user(user)
        return Response({
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh)
        })

class UserDeleteView(generics.DestroyAPIView):
    queryset = myuser.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self):
        return myuser.objects.get(username=self.request.user.username)
