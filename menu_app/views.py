from django.shortcuts import render
from django.views import View

class MenuView(View):
    def get(self, request, slug):
        return render(request, 'index.html')
