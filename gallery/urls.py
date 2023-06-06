from django.urls import path
from gallery.views import index, image, search

urlpatterns = [
    path('', index, name='home'),
    path('image/<int:picture_id>', image, name='image'),
    path('search', search, name='search'),
]