from django import http
from django.template import (Context, RequestContext,
                             loader, TemplateDoesNotExist)

try:
    from functools import wraps
except ImportError:
    from django.utils.functional import wraps

def user_owns(view_func):
    """
    Decorator for views that checks whether the user owns the currently requested
    resource.
    """
    @wraps(view_func)
    def _wrapped_view(request, username, *args, **kwargs):
        if hasattr(request.user, 'memberships'):
            usernames = [x.team.username for x in request.user.memberships.all()]
        else:
            usernames = []
        usernames.append(request.user.username)
        if username not in usernames:
            try:
                template = loader.get_template("403.html")
            except TemplateDoesNotExist:
                return http.HttpResponseForbidden('<h1>403 Forbidden</h1>')
            return http.HttpResponseForbidden(template.render(RequestContext(request)))
        return view_func(request, username=username, *args, **kwargs)
    return _wrapped_view
