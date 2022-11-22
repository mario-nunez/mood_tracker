import functools
from django.shortcuts import redirect


def authentication_not_required(view_func, redirect_url="home"):
    """
    This decorator checks if the user is logged in, if so it redirects
    him to the his 'home' view, if not it retrieves the page he was requesting.
    """
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        return redirect(redirect_url)
    return wrapper


def authentication_required(view_func, redirect_url="login"):
    """
    This decorator checks if the user is logged in, if so  it retrieves the
    page he was requesting, if not it redirects him to the login page.
    """
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        return redirect(redirect_url)
    return wrapper


def admin_only(view_func, redirect_url="home"):
    """
    This decorator checks if the user is admin, if not it redirects him to his
    home page.
    """
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        return redirect(redirect_url)
    return wrapper
