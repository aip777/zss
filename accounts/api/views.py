from rest_framework import generics, mixins, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
# from django.views.generic import View
from rest_framework.authentication import SessionAuthentication

from accounts.models import CustomUserModel
from .serializers import AccountSerializer


class CreateAccountAPI(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = AccountSerializer
    queryset                    = CustomUserModel.objects.all()

    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)