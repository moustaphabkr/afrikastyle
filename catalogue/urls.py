from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns  # <-- L'import magique pour les langues

# 1. Les routes qui ne doivent PAS changer de langue (l'administration et le système de switch)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),  # Permet au futur bouton FR/EN de fonctionner
]

# 2. Les routes de ton catalogue qui basculeront automatiquement entre /fr/ et /en/
urlpatterns += i18n_patterns(
    path('', include('catalogue.urls')),  # Inclut ton fichier proprement sans le modifier
)