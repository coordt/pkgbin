from django.contrib.auth.models import User
from django.conf.urls import url

from tastypie.authorization import Authorization
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie import fields
from tastypie.bundle import Bundle

from userpypi.models import Package, Release, Distribution, Classifier


# /user/{username}/packages/{packagename}/releases/{releasename}/files/{filepath}

from django.db import models
from tastypie.models import create_api_key

models.signals.post_save.connect(create_api_key, sender=User)


class UserResource(ModelResource):
    packages_owned = fields.ToManyField('api.PackageResource', 'packages_owned')
    
    class Meta:
        queryset = User.objects.exclude(username="AnonymousUser")
        resource_name = 'users'
        fields = ('first_name', 'last_name', 'username')
        allowed_methods = ['get']
    
    def get_resource_uri(self, bundle_or_obj):
        """
        Handles generating a resource URI for a single resource.

        Uses the model's ``username`` in order to create the URI.
        """
        kwargs = {
            'resource_name': self._meta.resource_name,
            'username': bundle_or_obj.obj.username
            if isinstance(bundle_or_obj, Bundle)
            else bundle_or_obj.username,
        }

        if self._meta.api_name is not None:
            kwargs['api_name'] = self._meta.api_name

        return self._build_reverse_url("api_dispatch_detail", kwargs=kwargs)
    
    def override_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/(?P<username>[\w\d_.-]+)/$" % self._meta.resource_name, self.wrap_view('dispatch_detail'), name="api_dispatch_detail"),
        ]

class PackageResource(ModelResource):
    owner = fields.ForeignKey(UserResource, 'owner')
    
    class Meta:
        queryset = Package.objects.all()
        resource_name = 'packages'
        # authentication = ApiKeyAuthentication()
        # authorization = Authorization()
        filtering = {
            'user': ALL_WITH_RELATIONS
        }
    
    def override_urls(self):
        return [
            url(r"^users/(?P<owner>[\w\d_.-]+)/(?P<resource_name>packages)/(?P<name>[\w\d_.-]+)/$", 
            self.wrap_view('dispatch_detail'), 
            name="api_dispatch_detail"),
        ]
    
    def obj_get(self, request=None, **kwargs):
        owner = kwargs.pop('owner')
        kwargs['owner__username'] = owner
        return super(PackageResource, self).obj_get(request, **kwargs)
    
    def get_resource_uri(self, bundle_or_obj):
        """
        Handles generating a resource URI for a single resource.
    
        Uses the model's ``name`` in order to create the URI.
        """
        kwargs = {
            'resource_name': self._meta.resource_name,
        }
        
        if isinstance(bundle_or_obj, Bundle):
            kwargs['name'] = bundle_or_obj.obj.name
            kwargs['owner'] = bundle_or_obj.obj.owner.username
        else:
            kwargs['name'] = bundle_or_obj.name
            kwargs['owner'] = bundle_or_obj.owner.username
    
        if self._meta.api_name is not None:
            kwargs['api_name'] = self._meta.api_name
    
        return self._build_reverse_url("api_dispatch_detail", kwargs=kwargs)
    # 
    # def obj_create(self, bundle, request=None, **kwargs):
    #     return super(PackageResource, self).obj_create(bundle, request, owner=request.user)
    # 
    # def apply_authorization_limits(self, request, object_list):
    #     return object_list.filter(owner=request.user)
