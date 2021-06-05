from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# Create your views here.
from appzss.forms import AddCountryForm
from appzss.models import Country

@login_required()
def addCountryView(request):
    if request.method == 'POST':
        form = AddCountryForm(request.POST, request.FILES)
        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.code = request.POST['name']
            form_data.save()
            messages.success(request, 'Successfully added')
            return redirect('country-list')
        else:
            messages.error(request, form.errors)
            return HttpResponseRedirect("#")
    else:
        country_form = AddCountryForm()
    
    context = {
        'form': country_form,
    }
    return render(request, 'country/add-country.html', context)


@login_required()
def countrylistView(request):
    country = Country.objects.all()
    context = {
        'country': country,
    }
    return render(request, 'country/country-list.html', context)

@login_required()
def updateCountryView(request, id):
    country = get_object_or_404(Country, id=id)
    if request.method == 'POST':
        form = AddCountryForm(request.POST, request.FILES, instance=country)

        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated')
            return redirect('country-list')
        else:
            messages.error(request, form.errors)
            return HttpResponseRedirect("#")
    else:
        form = AddCountryForm(instance=country)
    context = {
        'form': form,
    }
    return render(request, 'country/update-country.html', context)

@login_required()
def deleteCountryView(request, id):
    country = get_object_or_404(Country, id=id)
    country.delete()
    messages.success(request, 'Successfully deleted')
    return redirect('country-list')