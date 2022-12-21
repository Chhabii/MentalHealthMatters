from django.shortcuts import render
from .decorators import logout_required
# Create your views here.


@logout_required
def home(request):
    return render(request,'pages/home.html')