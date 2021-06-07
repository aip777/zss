from django.contrib.auth import authenticate
from rest_framework import generics, mixins, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
# from django.views.generic import View
from rest_framework.authentication import SessionAuthentication

from accounts.models import CustomUserModel
from .serializers import AccountSerializer
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout

User = get_user_model()

class AuthView(APIView):
    permission_classes          = [permissions.AllowAny]
    
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response({"details": "You are already authenticated"}, status=400)
        data = request.data
        email = data.get("email")
        password = data.get("password")
        user = authenticate(email=email, password=password)
        response = login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return Response(response)


class RegisterAPIView(APIView):
    permission_classes          = [permissions.AllowAny]
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response("details: You are already authenticated")
        data = request.data
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        password2 = data.get("password")
        is_active =True
        qs = CustomUserModel.objects.filter(Q(username__iexact=username)| Q(email__iexact=email))

        if password != password2:
            return Response({"details": "Password must match"}, status=401)

        if qs.exists():
            return Response({"details": "User already exists"}, status=401)
        
        else:
            user = CustomUserModel.objects.create(username=username, email=email,is_active=is_active)
            user.set_password(password)
            user.save()
            return Response(request)
        return Response({"details": "Invalid Request"}, status=400)