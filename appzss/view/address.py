from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# Create your views here.
from appzss.forms import AddAddressForm
from appzss.models import Address


@login_required()
def addAddressView(request):
    if request.method == 'POST':
        form = AddAddressForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added')
            return redirect('address-list')
        else:
            messages.error(request, form.errors)
            return HttpResponseRedirect("#")
    else:
        address_form = AddAddressForm()
    
    context = {
        'form': address_form,
    }
    return render(request, 'address/add-address.html', context)


@login_required()
def addressListView(request):
    address = Address.objects.all()
    context = {
        'address_item': address,
    }
    return render(request, 'address/address-list.html', context)

@login_required()
def updateAddressView(request, id):
    address = get_object_or_404(Address, id=id)
    if request.method == 'POST':
        form = AddAddressForm(request.POST, request.FILES, instance=address)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated')
            return redirect('address-list')
        else:
            messages.error(request, form.errors)
            return HttpResponseRedirect("#")
    else:
        form = AddAddressForm(instance=address)
    context = {
        'form': form,
    }
    return render(request, 'address/update-address.html', context)

@login_required()
def deleteAddressView(request, id):
    address = get_object_or_404(Address, id=id)
    address.delete()
    messages.success(request, 'Successfully deleted')
    return redirect('address-list')