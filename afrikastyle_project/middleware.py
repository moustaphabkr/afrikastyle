import os
from django.http import HttpResponse

class MaintenanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Vérifie la variable d'environnement
        # On force la lecture en chaîne de caractères pour éviter les erreurs
        maintenance = os.environ.get('MAINTENANCE_MODE', 'False')
        
        if maintenance == 'True':
            # Assure-toi que le chemin vers maintenance.html est correct
            return render(request, 'maintenance.html')
        
        return self.get_response(request)