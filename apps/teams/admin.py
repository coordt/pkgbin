from django.contrib import admin

from teams.models import TeamMember

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('team', 'user',)

admin.site.register(TeamMember, TeamMemberAdmin)
