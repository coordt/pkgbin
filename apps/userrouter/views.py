from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, DetailView, UpdateView

from djangopypi.models import Package, Release

class PackageListView(ListView):
    model = Package
    context_object_name = 'package_list'
    simple = False
    username = None
    
    def get_queryset(self):
        self.username = self.kwargs['username']
        if self.request.user.username != self.username:
            return self.model.objects.filter(owner__username=self.username, private=False)
        return self.model.objects.filter(owner=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super(PackageListView, self).get_context_data(**kwargs)
        context['username'] = self.kwargs.get('username', None)
        context['is_owner'] = self.username == self.request.user.username
        return context
    
    def get_template_names(self):
        """
        Returns a list of template names to be used for the request. Must return
        a list. May not be called if render_to_response is overridden.
        """
        if self.simple:
            return ['djangopypi/package_list_simple.html']
        else:
            return ['djangopypi/package_list.html']

class PackageDetailView(DetailView):
    model = Package
    context_object_name = 'package'
    simple = False
    doap = False
    username = None
    
    def render_to_response(self, context, **response_kwargs):
        """
        Returns a response with a template rendered with the given context.
        """
        if self.doap:
            response_kwargs['mimetype'] = 'text/xml'
        
        return super(PackageDetailView, self).render_to_response(context, **response_kwargs)
    
    def get_queryset(self):
        username = self.kwargs.get('username', None)
        if self.request.user.username != self.username:
            return self.model.objects.filter(owner__username=username, private=False)
        return self.model.objects.filter(owner=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super(PackageDetailView, self).get_context_data(**kwargs)
        context['username'] = self.kwargs.get('username', None)
        context['is_owner'] = self.username == self.request.user.username
        return context
    
    def get_object(self):
        package = self.kwargs.get('package', None)
        try:
            queryset = self.get_queryset().filter(name=package)
            obj = queryset.get()
        except ObjectDoesNotExist:
            raise Http404(_(u"No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._meta.verbose_name})
        return obj
    
    def get_template_names(self):
        """
        Returns a list of template names to be used for the request. Must return
        a list. May not be called if render_to_response is overridden.
        """
        if self.simple:
            return ['djangopypi/package_detail_simple.html']
        elif self.doap:
            return ['djangopypi/package_doap.xml']
        else:
            return ['djangopypi/package_detail.html']


class PackageManageView(UpdateView):
    model = Package
    context_object_name = 'package'
    template_name = 'djangopypi/package_manage.html'
    
    def get_queryset(self):
        self.username = self.kwargs['username']
        if self.request.user.username != self.username:
            return self.model.objects.filter(owner__username=self.username, private=False)
        return self.model.objects.filter(owner=self.request.user)
    
    def get_object(self):
        package = self.kwargs.get('package', None)
        try:
            queryset = self.get_queryset().filter(name=package)
            obj = queryset.get()
        except ObjectDoesNotExist:
            raise Http404(_(u"No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._meta.verbose_name})
        return obj


class ReleaseListView(ListView):
    model = Release
    context_object_name = 'release_list'
    simple = False
    username = None
    
    def get_queryset(self):
        self.username = self.kwargs['username']
        if self.request.user.username != self.username:
            return self.model.objects.filter(owner__username=self.username, private=False)
        return self.model.objects.filter(owner=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super(ReleaseListView, self).get_context_data(**kwargs)
        context['username'] = self.kwargs.get('username', None)
        context['is_owner'] = self.username == self.request.user.username
        return context
    
    def get_template_names(self):
        """
        Returns a list of template names to be used for the request. Must return
        a list. May not be called if render_to_response is overridden.
        """
        if self.simple:
            return ['djangopypi/release_list_simple.html']
        else:
            return ['djangopypi/release_list.html']
        

class ReleaseDetailView(DetailView):
    model = Release
    context_object_name = 'release'
    doap = False
    username = None
    
    def render_to_response(self, context, **response_kwargs):
        """
        Returns a response with a template rendered with the given context.
        """
        if self.doap:
            response_kwargs['mimetype'] = 'text/xml'
        
        return super(ReleaseDetailView, self).render_to_response(context, **response_kwargs)
    
    def get_queryset(self):
        username = self.kwargs.get('username', None)
        if self.request.user.username != username:
            return self.model.objects.filter(package__owner__username=username, package__private=False)
        return self.model.objects.filter(package__owner=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super(ReleaseDetailView, self).get_context_data(**kwargs)
        context['username'] = self.kwargs.get('username', None)
        context['is_owner'] = self.username == self.request.user.username
        return context
    
    def get_object(self):
        package = self.kwargs.get('package', None)
        try:
            queryset = self.get_queryset().filter(package__name=package)
            obj = queryset.get()
        except ObjectDoesNotExist:
            raise Http404(_(u"No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._meta.verbose_name})
        return obj
    
    def get_template_names(self):
        """
        Returns a list of template names to be used for the request. Must return
        a list. May not be called if render_to_response is overridden.
        """
        if self.doap:
            return ['djangopypi/release_doap.xml']
        else:
            return ['djangopypi/release_detail.html']
