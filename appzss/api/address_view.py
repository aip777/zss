from rest_framework import generics, mixins, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
# from django.views.generic import View
from rest_framework.authentication import SessionAuthentication

from appzss.models import Country, State, Address
from .serializers import AddressSerializer, StateSerializer


class AddressListAPI(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = AddressSerializer

    def get_queryset(self):
        qs = Address.objects.all()
        state = State.objects.all()
        state_obj = self.request.GET.get('state')

        house_number = self.request.GET.get('house')
        road_number = self.request.GET.get('road')
        if house_number is not None:
            qs = qs.filter(house_number__icontains=house_number)
        elif road_number is not None:
            qs = qs.filter(road_number__icontains=road_number)
        
        elif state_obj is not None:
            state_item = state.filter(name__icontains=state_obj)
            for id in state_item:
                qs = qs.filter(state=id.id)
        return qs
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        

class AddressDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
    permission_classes          = []
    authentication_classes      = []
    queryset                    = Address.objects.all()
    serializer_class            = AddressSerializer
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)