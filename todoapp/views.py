from django.shortcuts import render
from django.shortcuts import (
    get_list_or_404,
    get_object_or_404,
    HttpResponseRedirect,
    render,
)
from django.http import JsonResponse
from django.urls import reverse
from django.core import serializers
from django.utils.dateparse import parse_date
import json
from django.http import HttpResponse


from .models import Todo
from .forms import TodoCreationForm


def get_todos(request):

    todos = get_list_or_404(Todo, is_deleted=False)

    return render(request, "list.html", context={"todos": todos})


def get_todo(request, id):

    todo = get_object_or_404(Todo, id=id, is_deleted=False)

    return render(request, "read.html", context={"todo": todo})


def edit_todo(request, id):

    todo = get_object_or_404(Todo, id=id, is_deleted=False)

    if request.method != "POST":
        todo_form = TodoCreationForm()
        return render(
            request, "edit.html", context={"id": todo.id, "todo_form": todo_form}
        )
    else:
        todo_form = TodoCreationForm(request.POST)
        if todo_form.is_valid():
            data = request.POST
            print(request.POST)
            todo.title = data["title"]
            todo.description = data["description"]
            due_date_month = (
                "0" + data["due_date_month"]
                if data["due_date_month"] < "10"
                else data["due_date_month"]
            )
            due_date_day = (
                "0" + data["due_date_day"]
                if data["due_date_day"] < "10"
                else data["due_date_day"]
            )
            due_date_year = data["due_date_year"]
            date_str = due_date_year + "-" + due_date_month + "-" + due_date_day
            todo.due_date = parse_date(date_str)
            todo.status = data["status"]
            todo.save()

        return HttpResponseRedirect(reverse("get_todos"))


def delete_todo(request, id):

    todo = get_object_or_404(Todo, id=id, is_deleted=False)
    todo.is_deleted = True
    todo.save()

    return HttpResponseRedirect(reverse("get_todos"))


def create_todo(request):

    if request.method == "GET":
        todo_form = TodoCreationForm()
    elif request.method == "POST":
        todo_form = TodoCreationForm(request.POST)
        if todo_form.is_valid():
            data = request.POST
            title = data["title"]
            description = data["description"]
            due_date_month = (
                "0" + data["due_date_month"]
                if data["due_date_month"] < "10"
                else data["due_date_month"]
            )
            due_date_day = (
                "0" + data["due_date_day"]
                if data["due_date_day"] < "10"
                else data["due_date_day"]
            )
            due_date_year = data["due_date_year"]
            date_str = due_date_year + "-" + due_date_month + "-" + due_date_day
            due_date = parse_date(date_str)
            status = data["status"]
            todo = Todo(
                title=title, description=description, due_date=due_date, status=status
            )
            todo.save()
            return HttpResponseRedirect(reverse("get_todos"))

    return render(request, "create.html", {"todo_form": todo_form})


def get_api_todos(request):

    todos = serializers.serialize("json", Todo.objects.filter(is_deleted=False))
    print(todos)
    return HttpResponse(todos, content_type="application/json")


def get_api_todo(request, id):

    object_ = get_object_or_404(Todo, id=id)
    todo = serializers.serialize("json", Todo.objects.filter(id=id, is_deleted=False))

    return HttpResponse(todo, content_type="application/json")
