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
    for i in form.visible_fields():
        for j in i:
            print(j)
            print(j.data)
            print(type(j.data))
        break
    return render(request, "home.html", context)
