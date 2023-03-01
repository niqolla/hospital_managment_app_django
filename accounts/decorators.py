from django.http import HttpResponse
from django.shortcuts import redirect

def unathenticated_user(view_func):
    def wrapper_fuc(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_fuc

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None

            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else: 
                return HttpResponse('You do not permissions to view this page!')
        return wrapper_func
    return decorator
