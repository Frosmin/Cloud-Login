from django.shortcuts import render


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import View

class MensageView(View):
    def get(self, request, *args, **kwargs):
        
        return render(request, 'mensage.html')