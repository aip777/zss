from rest_framework import generics, mixins, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
# from django.views.generic import View
from rest_framework.authentication import SessionAuthentication

from appzss.models import Country, State, Address
from .serializers import StateSerializer


class StateListAPI(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = StateSerializer

    def get_queryset(self):
        qs = State.objects.all()
        country_obj = Country.objects.all()
        state_obj = self.request.GET.get('state')
        country = self.request.GET.get('country')
         
        if state_obj is not None:
            qs = qs.filter(name__icontains=state_obj)
        
        elif country is not None:
            country_obj = country_obj.filter(name__icontains=country)
            for contry_id in country_obj:
                qs = qs.filter(country=contry_id.id)
        return qs
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        

class StateDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
    permission_classes          = []
    authentication_classes      = []
    queryset                    = State.objects.all()
    serializer_class            = StateSerializer
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)