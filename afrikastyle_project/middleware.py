import os
from django.shortcuts import render 

class MaintenanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Vérification du mode maintenance
        if os.environ.get('MAINTENANCE_MODE') == 'True':
            return render(request, 'maintenance.html')
        
        return self.get_response(request)