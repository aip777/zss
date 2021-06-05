from django import forms
from .models import Country, State, Address
# external admin form start

class AddCountryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddCountryForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Country
        fields = (
                'id',
                'name',
                'latitude',
                'longitude'
            )

class AddStateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddStateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = State
        fields = (
                'id',
                'country',
                'name'
            )

class AddAddressForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddAddressForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Address
        fields = (
                'id',
                'name',
                'state',
                'house_number',
                'road_number'
            )