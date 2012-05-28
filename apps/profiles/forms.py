from userena.forms import EditProfileForm

class LimitedEditProfileForm(EditProfileForm):
    class Meta(EditProfileForm.Meta):
        exclude = ['user', 'organization', 'group', 'creator_id', 'privacy']