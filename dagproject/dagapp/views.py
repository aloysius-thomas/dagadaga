from django.shortcuts import render

from .forms import UserCreateForm


# Create your views here.
def create(request):
    form = UserCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        "forms": form,
    }
    return render(request, "home.html", context)
