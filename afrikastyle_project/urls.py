from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

# Routes globales sans traduction
urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
]

# Routes du catalogue avec traduction automatique
urlpatterns += i18n_patterns(
    path('', include('catalogue.urls')),
)