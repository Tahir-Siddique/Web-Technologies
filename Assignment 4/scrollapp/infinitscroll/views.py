from django.http.response import Http404, HttpResponse, JsonResponse
from django.shortcuts import render
def index(request):
    return render(request,'infinitscroll/index.html',{})
def generator(request):
    fakeposts = []
    if request.method=="GET":
        start = int(request.GET['start'] or 0)
        end = int(request.GET['end'] or 0+10)
        for i in range(start,end):
            fakeposts.append(f"Fake Post {i}")
        return JsonResponse(fakeposts,safe=False)
    return HttpResponse("<p>Invalid Request</p>")