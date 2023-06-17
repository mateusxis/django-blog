from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from gallery.models import Picture

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "User não logado")
        return redirect('login')
    
    pictures = Picture.objects.order_by("-date_picture").filter(published=True)
    return render(request, 'gallery/index.html', {"pictures": pictures})

def image(request, picture_id):
    if not request.user.is_authenticated:
        messages.error(request, "User não logado")
        return redirect('login')
    
    picture = get_object_or_404(Picture, pk=picture_id) 
    return render(request, 'gallery/image.html', {"picture": picture})

def search(request):
    if not request.user.is_authenticated:
        messages.error(request, "User não logado")
        return redirect('login')
        
    pictures = Picture.objects.order_by("-date_picture").filter(published=True)

    if "term" in request.GET:
        term = request.GET["term"]
        if term:
            pictures = pictures.filter(name__icontains=term)
    return render(request, 'gallery/search.html', {"pictures": pictures})
