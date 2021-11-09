from django.shortcuts import redirect, render
from . import util
import random as rd
# Create your views here.


def index(request):
    return render(request, "outline/index.html", {
        "topics": util.list_topics(),
        "isIndexPage": True,
    })


def random(request):
    return redirect(f"/{rd.choice(util.list_topics())}")


def createNewPage(request):
    title = ""
    content = ""
    isExist = False
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        if title not in util.list_topics():
            util.save_topic(title, content)
            return redirect(f"/{title}")

        else:
            isExist = True
    return render(request, "outline/createnewpage.html", {
        "isExist": isExist,
    })


def editPage(request):
    title = ""
    content = ""
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        util.save_topic(title, content)
        return redirect(f"/{title}")

    if request.method == "GET":
        title = request.GET.get("title")
        content = util.get_topic(title)

    return render(request, "outline/editpage.html", {
        "title": title,
        "content": content,
    })


def getByTitle(request, TITLE):
    isTopicExist = False
    topic = util.get_topic(TITLE)
    if topic is not None:
        isTopicExist = True
    else:
        isTopicExist = False
    return render(request, "outline/index.html", {
        "topics": util.list_topics(),
        "topic": topic,
        "isTopicExist": isTopicExist,
        "title": TITLE,
        "isIndexPage": False,
    })


def searchByTitle(request):
    isTopicExist = False
    topics = None
    q = ""
    if request.method == "GET":
        q = request.GET.get("q")
        topics = util.get_topic(q)
        if topics is not None:
            print(topics)
            return redirect(f"/{q}")

        else:
            topics = [k for k in util.list_topics() if q in k]
    return render(request, "outline/search.html", {
        "q": q,
        "topics": topics,
    })
