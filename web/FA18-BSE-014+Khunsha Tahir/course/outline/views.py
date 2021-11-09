from random import randint
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import messages
from django import forms
from markdown2 import Markdown

from . import util


class NewtopicsForm(forms.Form):
    title = forms.CharField(
        required=True,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Title", "class": "mb-4"}
        ),
    )
    content = forms.CharField(
        required=True,
        label="",
        widget=forms.Textarea(
            attrs={
                "class": "form-control mb-4",
                "placeholder": "Content (markdown)",
                "id": "new_content",
            }
        ),
    )


def index(request):
    return render(
        request, "outline/index.html", {"topics": util.list_topics()}
    )


def outline(request, topics):
    if topics not in util.list_topics():
        raise Http404
    content = util.get_topics(topics)
    return render(
        request,
        "outline/outline.html",
        {"title": topics, "content": Markdown().convert(content)},
    )


def search(request):
    query = request.GET.get("q", "")
    if query is None or query == "":
        return render(
            request,
            "outline/search.html",
            {"found_topics": "", "query": query},
        )

    topics = util.list_topics()

    found_topics = [
        valid_topics
        for valid_topics in topics
        if query.lower() in valid_topics.lower()
    ]
    if len(found_topics) == 1:
        return redirect("outline", found_topics[0])

    return render(
        request,
        "outline/search.html",
        {"found_topics": found_topics, "query": query},
    )


def new(request):
    if request.method == "GET":
        return render(
            request, "outline/new.html", {"form": NewtopicsForm()}
        )

    form = NewtopicsForm(request.POST)
    if form.is_valid():
        title = form.cleaned_data.get("title")
        content = form.cleaned_data.get("content")

        if title.lower() in [topics.lower() for topics in util.list_topics()]:
            messages.add_message(
                request,
                messages.WARNING,
                message=f'topics "{title}" already exists',
            )
        else:
            with open(f"topics/{title}.md", "w") as file:
                file.write(content)
            return redirect("outline", title)

    else:
        messages.add_message(
            request, messages.WARNING, message="Invalid request form"
        )

    return render(
        request,
        "outline/new.html",
        {"form": form},
    )


def random_topics(request):
    topics = util.list_topics()
    topics = topics[randint(0, len(topics) - 1)]
    return redirect("outline", topics)


def edit(request, topics):
    if request.method == "GET":
        title = topics
        content = util.get_topics(title)
        form = NewtopicsForm({"title": title, "content": content})
        return render(
            request,
            "outline/edit.html",
            {"form": form, "title": title},
        )

    form = NewtopicsForm(request.POST)
    if form.is_valid():
        title = form.cleaned_data.get("title")
        content = form.cleaned_data.get("content")

        util.save_topics(title=title, content=content)
        return redirect("outline", title)


def handler404(request, *args):
    return render(request, "404.html", {})
