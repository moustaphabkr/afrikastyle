import os
from django.shortcuts import render

class MaintenanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # On vérifie la variable d'environnement (par défaut False)
        if os.getenv('MAINTENANCE_MODE', 'False') == 'True':
           # Modifie la ligne 11 dans afrikastyle_project/middleware.py
            return render(request, 'catalogue/maintenance.html', status=503)
        
        return self.get_response(request)