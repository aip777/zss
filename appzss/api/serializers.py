from rest_framework import serializers
from appzss.models import Country, State, Address



class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields =[
            'id'
            'name',
            'latitude',
            'longitude',
            'code'
        ]
        read_only_fields = ("code",)


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields =[
            'id',
            'name',
            'country',
        ]
    

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields =[
            'id',
            'name',
            'state',
            'house_number',
            'road_number',
        ]