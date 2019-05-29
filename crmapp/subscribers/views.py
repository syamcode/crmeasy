from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import SubscireberForm

def subscriber_new(request, template='subscribers/subscriber_new.html'):
    if request.method == 'POST':
        form = SubscireberForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']

            user = User(username=username, email=email)
            user.set_password(password)
            user.save()

            return HttpResponseRedirect('/success/')
    else:
        form = SubscireberForm()

    return render(request, template, {'form':form})
