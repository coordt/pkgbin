from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from admin_tools.menu.models import *

class CustomMenu(Menu):
    def __init__(self, **kwargs):
        super(CustomMenu, self).__init__(**kwargs)
        self.children = (
            MenuItem(title='Dashboard', url=reverse('admin:index')),
            AppListMenuItem(title='Applications'),
            MenuItem(title='Packages', children=[
                MenuItem(title='Packages', url=reverse('admin:userpypi_package_changelist')),
                MenuItem(title='Releases', url=reverse('admin:userpypi_release_changelist')),
                MenuItem(title='Distributions', url=reverse('admin:userpypi_distribution_changelist')),
                MenuItem(title='Classifiers', url=reverse('admin:userpypi_package_changelist')),
            ]),
            # MenuItem(title='Organize', children=[
            #     MenuItem(title='Navigation Bar', url=reverse('admin:navbar_navbarentry_changelist')),
            # ]),
            MenuItem(title='Settings', children=[
                # MenuItem(title='Analytics', url=reverse('admin:google_analytics_analytics_changelist')),
                # MenuItem(title='Redirects', url=reverse('admin:redirects_redirect_changelist')),
                MenuItem(title='Robots', url=reverse('admin:app_list', args=('robots',))),
            ]),
            MenuItem(title='Users', children=[
                MenuItem(title='Users', url=reverse('admin:auth_user_changelist')),
                MenuItem(title='Groups', url=reverse('admin:auth_group_changelist')),
                MenuItem(title='Profiles', url=reverse('admin:profiles_profile_changelist')),
            ])
            
        )
