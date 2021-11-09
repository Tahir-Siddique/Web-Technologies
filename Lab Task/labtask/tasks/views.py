from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls.base import reverse


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)
# Create your views here.


tasks = []


def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })


def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("index"))
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })


def delete(request):
    if request.method == "GET":
        task = request.GET.get("task")
        del request.session["tasks"][request.session["tasks"].index(task)]
        return HttpResponseRedirect(reverse("index"))
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })
