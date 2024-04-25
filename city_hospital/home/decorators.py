# decorators.py

from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden
from django.contrib.auth.models import Group
from django.contrib.auth import logout
from django.shortcuts import redirect

# decorators.py

from django.contrib.auth.decorators import user_passes_test

def groups_required(group_names):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            # Check if the user belongs to any of the specified groups
            if request.user.groups.filter(name__in=group_names).exists():
                return view_func(request, *args, **kwargs)
            else:
                # Redirect to a forbidden page or display an error message
                logout(request)
                return HttpResponseForbidden("You do not have permission to access this page.")
        return wrapper
    return decorator
