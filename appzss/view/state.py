from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# Create your views here.
from appzss.forms import AddStateForm
from appzss.models import State


@login_required()
def addStateView(request):
    if request.method == 'POST':
        form = AddStateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added')
            return redirect('state-list')
        else:
            messages.error(request, form.errors)
            return HttpResponseRedirect("#")
    else:
        state = AddStateForm()
    
    context = {
        'form': state,
    }
    return render(request, 'state/add-state.html', context)


@login_required()
def statelistView(request):
    state = State.objects.all()
    context = {
        'state': state,
    }
    return render(request, 'state/state-list.html', context)

@login_required()
def updateStateView(request, id):
    state = get_object_or_404(State, id=id)
    if request.method == 'POST':
        form = AddStateForm(request.POST, request.FILES, instance=state)

        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated')
            return redirect('state-list')
        else:
            messages.error(request, form.errors)
            return HttpResponseRedirect("#")
    else:
        form = AddStateForm(instance=state)
    context = {
        'form': form,
    }
    return render(request, 'state/update-state.html', context)

@login_required()
def deleteStateView(request, id):
    state = get_object_or_404(State, id=id)
    state.delete()
    messages.success(request, 'Successfully deleted')
    return redirect('state-list')