from django.contrib import admin
from django.urls import path, include # <-- On a ajouté "include" ici

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalogue.urls')), # <-- On connecte les URLs du catalogue
]