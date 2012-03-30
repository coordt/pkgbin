from django.conf.urls.defaults import *
from djangopypi.feeds import ReleaseFeed
from .views import PackageListView, PackageDetailView, ReleaseDetailView, PackageManageView

from userena.settings import USERENA_ACTIVATION_REQUIRED, USERENA_ACTIVATION_DAYS

urlpatterns = patterns('',
    
    # Basic Package Indexes
    url(r'^(?P<username>[^/]+)/$',
        PackageListView.as_view(),
        name="userrouter-index"),
    url(r'^(?P<username>[^/]+)/packages/$',
        PackageListView.as_view(), 
        name='userpypi-package-index'),
    
    # url(r'^(?P<username>[^/]+)/search/$',
    #     'packages.search',
    #     name='userpypi-search'),
    url(r'^(?P<username>[^/]+)/rss/$', 
        ReleaseFeed(), 
        name='userpypi-rss'),
    
    # Simple indexes
    url(r'^(?P<username>[^/]+)/simple/$',
        PackageListView.as_view(simple=True),
        name='userpypi-package-index-simple'),
    url(r'^(?P<username>[^/]+)/simple/(?P<package>[\w\d_\.\-]+)/$',
        PackageDetailView.as_view(simple=True),
        name='userpypi-package-simple'),
    
    # Regular Indexes
    url(r'^(?P<username>[^/]+)/pypi/$', 
        'djangopypi.views.root', 
        name="userpypi-root"),
    url(r'^(?P<username>[^/]+)/pypi/(?P<package>[\w\d_\.\-]+)/$',
        PackageDetailView.as_view(),
        name='userpypi-package'),
    url(r'^(?P<username>[^/]+)/pypi/(?P<package>[\w\d_\.\-]+)/rss/$', 
        ReleaseFeed(),
        name='userpypi-package-rss'),    
    url(r'^(?P<username>[^/]+)/pypi/(?P<package>[\w\d_\.\-]+)/doap.rdf$',
        PackageDetailView.as_view(doap=True),
        name='userpypi-package-doap'),
    url(r'^(?P<username>[^/]+)/pypi/(?P<package>[\w\d_\.\-]+)/manage/$',
        PackageManageView.as_view(),
        name='userpypi-package-manage'),
    # url(r'^(?P<username>[^/]+)/pypi/(?P<package>[\w\d_\.\-]+)/manage/versions/$',
    #     'packages.manage_versions',
    #     name='userpypi-package-manage-versions'),
    url(r'^(?P<username>[^/]+)/pypi/(?P<package>[\w\d_\.\-]+)/(?P<version>[\w\d_\.\-]+)/$',
        ReleaseDetailView.as_view(),
        name='userpypi-release'),
    url(r'^(?P<username>[^/]+)/pypi/(?P<package>[\w\d_\.\-]+)/(?P<version>[\w\d_\.\-]+)/doap.rdf$',
        ReleaseDetailView.as_view(doap=True),
        name='userpypi-release-doap'),
    # url(r'^(?P<username>[^/]+)/pypi/(?P<package>[\w\d_\.\-]+)/(?P<version>[\w\d_\.\-]+)/manage/$',
    #     'releases.manage',
    #     name='djangopypi-release-manage'),
    # url(r'^(?P<username>[^/]+)/pypi/(?P<package>[\w\d_\.\-]+)/(?P<version>[\w\d_\.\-]+)/metadata/$',
    #     'releases.manage_metadata',
    #     name='djangopypi-release-manage-metadata'),
    # url(r'^(?P<username>[^/]+)/pypi/(?P<package>[\w\d_\.\-]+)/(?P<version>[\w\d_\.\-]+)/files/$',
    #     'releases.manage_files',
    #     name='userpypi-release-manage-files'),
    # url(r'^(?P<username>[^/]+)/pypi/(?P<package>[\w\d_\.\-]+)/(?P<version>[\w\d_\.\-]+)/files/upload/$',
    #     'releases.upload_file',
    #     name='userpypi-release-upload-file'),
    
    
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
    
)
