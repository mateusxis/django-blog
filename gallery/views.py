from django.shortcuts import render, get_object_or_404
from gallery.models import Picture

def index(request):
    pictures = Picture.objects.order_by("-date_picture").filter(published=True)

    return render(request, 'gallery/index.html', {"pictures": pictures})

def image(request, picture_id):
    picture = get_object_or_404(Picture, pk=picture_id) 
    return render(request, 'gallery/image.html', {"picture": picture})

def search(request):
    pictures = Picture.objects.order_by("-date_picture").filter(published=True)

    if "term" in request.GET:
        term = request.GET["term"]
        if term:
            pictures = pictures.filter(name__icontains=term)
    return render(request, 'gallery/search.html', {"pictures": pictures})
