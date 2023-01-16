from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Students

def homepage(req):
    form = StudentForm(req.POST or None)
    if req.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(homepage)

    return render(req, "home.html", {"form":form, "students": Students.objects.all()})