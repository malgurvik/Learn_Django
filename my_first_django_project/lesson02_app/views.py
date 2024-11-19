from django.contrib.messages.context_processors import messages
from django.shortcuts import render
from django.http import HttpResponse
from .forms import AuthorForm
from .models import Author


def index(request):
    return render(request, "lesson02_app/base.html")


def add_new_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            biography = form.cleaned_data["biography"]
            birth_date = form.cleaned_data["birth_date"]
            author = Author.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                biography=biography,
                birth_date=birth_date,
            )
            author.save()
            message = "Author created successfully"
            return render(request, "lesson02_app/add_new_author.html", {"message": message})
    else:
        message = "Add a new author"
        form = AuthorForm()
        return render(
            request,
            "lesson02_app/add_new_author.html",
            {"form": form, "message": message},
        )
