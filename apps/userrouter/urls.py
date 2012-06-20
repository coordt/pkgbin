from django.conf.urls.defaults import *
from django.views.generic.base import TemplateView

from userena.settings import USERENA_ACTIVATION_REQUIRED, USERENA_ACTIVATION_DAYS
from userena import views
from userpypi.views.packages import PackageListView
from userrouter.decorators import user_owns
from profiles.forms import LimitedEditProfileForm

urlpatterns = patterns('',
    url(r'^(?P<username>[^/]+)/$',
        user_owns(views.direct_to_user_template),
        {'template_name':"user_home.html"},
        name="userrouter-index"),
    
    # User Signup
    url(r'^(?P<username>[\.\w]+)/signup/complete/$',
        views.direct_to_user_template,
        {'template_name': 'userena/signup_complete.html',
        'extra_context': {'userena_activation_required': USERENA_ACTIVATION_REQUIRED,
                          'userena_activation_days': USERENA_ACTIVATION_DAYS}},
        name='userena_signup_complete'),

    # User Activate
    url(r'^(?P<username>[\.\w]+)/activate/(?P<activation_key>\w+)/$',
        views.activate,
        name='userena_activate'),

    # Change email and confirm it
    url(r'^(?P<username>[\.\w]+)/email/$',
       user_owns(views.email_change),
       name='userena_email_change'),
    url(r'^(?P<username>[\.\w]+)/email/complete/$',
       user_owns(views.direct_to_user_template),
       {'template_name': 'userena/email_change_complete.html'},
       name='userena_email_change_complete'),
    url(r'^(?P<username>[\.\w]+)/confirm-email/complete/$',
       user_owns(views.direct_to_user_template),
       {'template_name': 'userena/email_confirm_complete.html'},
       name='userena_email_confirm_complete'),
    url(r'^(?P<username>[\.\w]+)/confirm-email/(?P<confirmation_key>\w+)/$',
       user_owns(views.email_confirm),
       name='userena_email_confirm'),

    # Disabled account
    url(r'^(?P<username>[\.\w]+)/disabled/$',
       'userena.views.direct_to_user_template',
       {'template_name': 'userena/disabled.html'},
       name='userena_disabled'),

    # Change password
    url(r'^(?P<username>[\.\w]+)/password/$',
        user_owns(views.password_change),
        name='userena_password_change'),
    url(r'^(?P<username>[\.\w]+)/password/complete/$',
        user_owns(views.direct_to_user_template),
        {'template_name': 'userena/password_complete.html'},
        name='userena_password_change_complete'),
    
    # Edit profile
    url(r'^(?P<username>[\.\w]+)/edit/$',
        user_owns(views.profile_edit),
        {'edit_profile_form': LimitedEditProfileForm},
        name='userena_profile_edit'),
    
    url(r'^(?P<username>[^/]+)/profile/$',
        'userena.views.profile_detail',
        name='userena_profile_detail'),
    
    ('', include('userpypi.urls')),
)
