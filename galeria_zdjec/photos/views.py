from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import PhotoForm
from .models import Photo

from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)


def photo_list(request):
    queryset = Photo.objects.all()
    context = {
        "photos": queryset,
    }
    return render(request, "home.html", context)


@login_required
def add_photo_view(request):
    form = PhotoForm()
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/u/" + request.user.username)
    context = {
        'form': form
    }
    return render(request, "add_photo.html", context)


@login_required
def delete_photo_list(request):
    queryset = Photo.objects.all()
    context = {
        "photos": queryset,
    }
    return render(request, "delete_photo.html", context)


@login_required
def delete_photo(request, pk):
    if request.method == 'POST':
        photo = Photo.objects.get(pk=pk)
        photo.delete()
    return redirect('delete_photo_list')


def profile(request, username):
    queryset = Photo.objects.all()
    if User.objects.get(username=username):
        u = User.objects.get(username=username)
        context = {
            "photos": queryset,
            "u": u,
        }
        return render(request, "gallery.html", context)
    else:
        return render("User not found")


def home(request):
    if request.user.is_authenticated:
        return redirect("/u/" + request.user.username)
    else:
        return redirect("/")

