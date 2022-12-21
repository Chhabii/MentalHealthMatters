from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
            return redirect('/')  # Redirect to the homepage
        return view_func(request, *args, **kwargs)
    return wrapper