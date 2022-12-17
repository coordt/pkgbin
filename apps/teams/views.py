from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext, loader

from teams.forms import TeamCreationForm, TeamUpdateForm, TeamMemberFormset
from teams.models import TeamMember
from profiles.models import Profile


def create_team(request, username):
    """
    Display the TeamCreationForm
    """
    if request.method == 'POST':
        form = TeamCreationForm(request.POST)
        if form.is_valid() and request.user.pk == form.cleaned_data['creator']:
            team = User.objects.create_user(form.cleaned_data['name'])
            team_creator_attrs = dict(
                team=team, 
                user=request.user, 
                permission=4, 
                creator=True
            )
            team_creator = TeamMember(**team_creator_attrs)
            team_creator.save()
            try:
                profile = team.get_profile()
            except Profile.DoesNotExist:
                profile = Profile(user=team)
            profile.organization = True
            profile.creator_id = request.user.pk
            profile.save()
            HttpResponseRedirect(reverse('update_team', args=(form.cleaned_data["name"],)))
    else:
        form = TeamCreationForm(initial={'creator': request.user.pk})
    return render_to_response('teams/team_create.html', 
        {'form': form, 'username': username},
        context_instance=RequestContext(request))

def update_team(request, username):
    """
    Display the TeamUpdateForm
    """
    template_name='teams/team_manage.html'

    obj = get_object_or_404(User, username=username)

    if not obj.get_profile().organization:
        raise Http404

    # Check that requesting user has admin privileges on this team
    if not request.user.has_perm('admin', obj):
        try:
            template = loader.get_template("403.html")
        except TemplateDoesNotExist:
            return http.HttpResponseForbidden('<h1>403 Forbidden</h1>')

    # Should prevent the deletion of the creator user. Not sure how to do this

    if request.method == 'POST':
        form = TeamUpdateForm(request.POST, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            member_formset = TeamMemberFormset(request.POST, instance=obj)
            if member_formset.is_valid():
                obj.save()
                member_formset.save()
                return HttpResponseRedirect(reverse('update_team', kwargs={'username': username}))
    else:
        form = TeamUpdateForm(instance=obj)
        member_formset = TeamMemberFormset(instance=obj)

    t = loader.get_template(template_name)
    c = RequestContext(request, {
        'form': form,
        'member_formset': member_formset,
        'profile': obj.get_profile(),
    })
    return HttpResponse(t.render(c))
    