from django.contrib import messages
from django.shortcuts import render
from django.views.decorators.http import require_POST

from .models import Gallery, Image
from .modelforms import GalleryForm, ImageForm


def index(request):
    galleries = Gallery.objects.filter()
    context = {"galleries": galleries}
    return render(request, 'app/index.html', context)


def gallery(request, id=None):
    gallery = Gallery.objects.get(id=id) if id else None
    if request.method == "POST":
        form = GalleryForm(request.POST, instance=gallery)
        if form.is_valid():
            form.save()
            messages.info(request, "Gallery saved")
            form = GalleryForm()
    else:
        form = GalleryForm(instance=gallery)
    context = {"gallery": gallery, "form": form}
    return render(request, 'app/gallery.html', context)


@require_POST
def gallery_delete(request, id):
    gallery = Gallery.objects.get(id=id)
    context = {"gallery": gallery}
    return render(request, 'app/gallery_delete.html', context)


def image(request, id=None):
    image = Image.objects.get(id=id) if id else None
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            messages.success(request, "Image saved")
            form = ImageForm()
    else:
        form = ImageForm(instance=image)
    context = {"gallery": gallery, "form": form}
    return render(request, 'app/image.html', context)


@require_POST
def image_delete(request, id):
    image = Gallery.objects.get(id=id)
    context = {"image": image}
    return render(request, 'app/image_delete.html', context)


