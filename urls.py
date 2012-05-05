import os

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from userena.settings import USERENA_REDIRECT_ON_SIGNOUT
from django.contrib.flatpages.models import FlatPage

admin.autodiscover()

sitemaps = {
}
flatpage_pattern = "|".join([x.strip("/") for x in FlatPage.objects.all().values_list('url', flat=True)])

from userrouter.decorators import user_owns
from userena import views

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^$', TemplateView.as_view(template_name='homepage.html')),
    (r'^admin_tools/', include('admin_tools.urls')),

    # Signup, signin and signout

    url(r'^signup/$',
        'userena.views.signup',
        name='userena_signup'),
    url(r'^signin/$',
        'userena.views.signin',
        name='userena_signin'),
    url(r'^signout/$',
        'django.contrib.auth.views.logout',
        {'next_page': USERENA_REDIRECT_ON_SIGNOUT,
        'template_name': 'userena/signout.html'},
        name='userena_signout'),
    
    url(r'^beta/$', 
        'hunger.views.invite', 
        name='beta_invite'),
    url(r'^beta/sent', 
        'hunger.views.confirmation', 
        name='beta_confirmation'),
    url(r'^beta/verify/(\w+)/$', 
        'hunger.views.verify_invite', 
        name='beta_verify'),
    url(r'^beta/expired', 
        'hunger.views.expired', 
        name='beta_used'),

    # Reset password
    url(r'^password/reset/$',
        'django.contrib.auth.views.password_reset',
        {'template_name': 'userena/password_reset_form.html',
        'email_template_name': 'userena/emails/password_reset_message.txt'},
        name='userena_password_reset'),
    url(r'^password/reset/done/$',
        'django.contrib.auth.views.password_reset_done',
        {'template_name': 'userena/password_reset_done.html'},
        name='userena_password_reset_done'),
    url(r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'template_name': 'userena/password_reset_confirm_form.html'},
        name='userena_password_reset_confirm'),
    url(r'^password/reset/confirm/complete/$',
        'django.contrib.auth.views.password_reset_complete',
        {'template_name': 'userena/password_reset_complete.html'}),
    
    url(r'^(?P<username>[\.\w]+)/edit/$',
        user_owns(views.profile_edit),
        name='userena_profile_edit'),
    
    url(r'^(?P<username>[^/]+)/profile/$',
        'userena.views.profile_detail',
        name='userena_profile_detail'),
    
    (r'(?P<url>%s/)' % flatpage_pattern, 'django.contrib.flatpages.views.flatpage'),
    (r'404/$', 'django.views.defaults.page_not_found'),
    (r'', include('userrouter.urls')),

)

# urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^media/static/(?P<path>.*)$', 'serve'),
    )
