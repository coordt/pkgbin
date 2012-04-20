from django.conf.urls.defaults import *

from userena.settings import USERENA_ACTIVATION_REQUIRED, USERENA_ACTIVATION_DAYS

from userpypi.views.packages import PackageListView

urlpatterns = patterns('',
    url(r'^(?P<owner>[^/]+)/$',
        PackageListView.as_view(),
        name="userrouter-index"),
    
    # User Signup
    url(r'^(?P<username>[\.\w]+)/signup/complete/$',
        'userena.views.direct_to_user_template',
        {'template_name': 'userena/signup_complete.html',
        'extra_context': {'userena_activation_required': USERENA_ACTIVATION_REQUIRED,
                          'userena_activation_days': USERENA_ACTIVATION_DAYS}},
        name='userena_signup_complete'),

    # User Activate
    url(r'^(?P<username>[\.\w]+)/activate/(?P<activation_key>\w+)/$',
        'userena.views.activate',
        name='userena_activate'),

    # Change email and confirm it
    url(r'^(?P<username>[\.\w]+)/email/$',
       'userena.views.email_change',
       name='userena_email_change'),
    url(r'^(?P<username>[\.\w]+)/email/complete/$',
       'userena.views.direct_to_user_template',
       {'template_name': 'userena/email_change_complete.html'},
       name='userena_email_change_complete'),
    url(r'^(?P<username>[\.\w]+)/confirm-email/complete/$',
       'userena.views.direct_to_user_template',
       {'template_name': 'userena/email_confirm_complete.html'},
       name='userena_email_confirm_complete'),
    url(r'^(?P<username>[\.\w]+)/confirm-email/(?P<confirmation_key>\w+)/$',
       'userena.views.email_confirm',
       name='userena_email_confirm'),

    # Disabled account
    url(r'^(?P<username>[\.\w]+)/disabled/$',
       'userena.views.direct_to_user_template',
       {'template_name': 'userena/disabled.html'},
       name='userena_disabled'),

    # Change password
    url(r'^(?P<username>[\.\w]+)/password/$',
        'userena.views.password_change',
        name='userena_password_change'),
    url(r'^(?P<username>[\.\w]+)/password/complete/$',
        'userena.views.direct_to_user_template',
        {'template_name': 'userena/password_complete.html'},
        name='userena_password_change_complete'),
    
    # Edit profile
    url(r'^(?P<username>[\.\w]+)/edit/$',
        'userena.views.profile_edit',
        name='userena_profile_edit'),
    
    ('', include('userpypi.urls')),
)
