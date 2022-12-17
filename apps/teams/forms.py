from django.contrib.auth.models import User
from django import forms
from django.forms.models import inlineformset_factory

from teams.models import TeamMember
from selectable.base import ModelLookup
from selectable.forms import AutoCompleteSelectField
from selectable.registry import registry, LookupAlreadyRegistered

class UserLookup(ModelLookup):
    model = User
    search_fields = (
        'username__icontains',
        'first_name__icontains',
        'last_name__icontains',
    )
    filters = {'is_active': True, }

    def get_item_value(self, item):
        # Display for currently selected item
        return item.username

    def get_item_label(self, item):
        # Display for choice listings
        return f"{item.username} ({item.get_full_name()})"
try:
    registry.register(UserLookup)
except LookupAlreadyRegistered:
    pass


class TeamCreationForm(forms.Form):
    """
    A form for creating an organziation
    """
    creator = forms.IntegerField(widget=forms.HiddenInput)
    name = forms.CharField(max_length=80)
    # email = forms.EmailField()
    
    def clean_name(self):
        org_name = self.cleaned_data['name']
        if User.objects.filter(username=org_name).count():
            raise forms.ValidationError(f'{org_name} is not a unique name.')
        return org_name


class TeamMemberForm(forms.ModelForm):
    user = AutoCompleteSelectField(lookup_class=UserLookup)
    
    class Meta:
        model = TeamMember
        exclude = ['creator'],
    
    def clean_user(self):
        """
        Make sure the user isn't already on the team
        """
        user = self.cleaned_data['user']
        team = self.cleaned_data['team']
        if self.initial and self.initial.has_key('user'):
            users = TeamMember.objects.filter(team=team, user=user).exclude(user__pk=self.initial['user']).count()
        else:
            users = TeamMember.objects.filter(team=team, user=user).count()
        if users > 0:
            raise forms.ValidationError(
                f"{user.username} is already a member of the team."
            )
        return user

TeamMemberFormset = inlineformset_factory(User, TeamMember, 
                                          fk_name='team', form=TeamMemberForm, extra=1)

class TeamUpdateForm(forms.ModelForm):
    """
    A form for updating an organziation
    """
    id = forms.IntegerField(widget=forms.HiddenInput)
    
    class Meta:
        model = User
        fields = ['id']
    