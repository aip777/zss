from rest_framework import generics, mixins, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
# from django.views.generic import View
from rest_framework.authentication import SessionAuthentication

from appzss.models import Country, State, Address
from .serializers import CountrySerializer
import pytz

# class CountryList(APIView):
#     permission_classes          = []
#     authentication_classes      = [SessionAuthentication]

#     def get(self, request, format=None):
#         qs = Country.objects.all()
#         serializer = CountrySerializer(qs, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         qs = Country.objects.all()
#         serializer = CountrySerializer(qs, many=True)
#         return Response(serializer.data)


class CountryListAPI(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = CountrySerializer

    def get_queryset(self):
        qs = Country.objects.all()
        country = self.request.GET.get('country')
        code = self.request.GET.get('code')

        if country is not None:
            qs = qs.filter(name__icontains=country)
        elif code is not None:
            qs = qs.filter(code__icontains=code)

        return qs
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        

# class CountryCreateAPIView(generics.CreateAPIView):
#     permission_classes          = []
#     authentication_classes      = []
#     queryset                    = Country.objects.all()
#     serializer_class            = CreateCountrySerializer


class CountryDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
    permission_classes          = []
    authentication_classes      = []
    queryset                    = Country.objects.all()
    serializer_class            = CountrySerializer
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)