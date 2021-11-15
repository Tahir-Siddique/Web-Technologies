from django.http.response import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.


flights = ["PIA"]


def index(request):
    context = {
        "name": "Tooba Naseem",
        "fname": "Muhammad Naseem",
        "flights": flights
    }
    return render(request, "flight/index.html", context)


def add(request):

    if request.method == "POST":
        flights.append(request.POST.get("flight_name"))
        return redirect("/flight")
    return render(request, "flight/add.html", context={})
