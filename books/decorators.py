from django.http import HttpResponseForbidden


def admin_required(view_func):

    def wrapper(request, *args, **kwargs):

        if request.user.groups.filter(name__in=["Admin", "SuperAdmin"]).exists():
            return view_func(request, *args, **kwargs)

        return HttpResponseForbidden("Permission Denied")

    return wrapper



def superadmin_required(view_func):

    def wrapper(request, *args, **kwargs):

        if request.user.groups.filter(name="SuperAdmin").exists():
            return view_func(request, *args, **kwargs)

        return HttpResponseForbidden("Permission Denied")

    return wrapper