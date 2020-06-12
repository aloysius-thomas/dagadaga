# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from forms import UserCreateForm

from django.shortcuts import render


# Create your views here.
def create(request):
    form = UserCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        "forms": form,
    }
    return render(request,"home.html",context)