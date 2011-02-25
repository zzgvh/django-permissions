from django.contrib import admin

from permissions.models import ObjectPermission
admin.site.register(ObjectPermission)

from permissions.models import Permission
admin.site.register(Permission)

from permissions.models import Role
admin.site.register(Role)

from permissions.models import PrincipalRoleRelation

class PrincipalRoleRelationAdmin(admin.ModelAdmin):
    list_display = ('principal', 'role', 'content_type', 'content')
    list_filter = ('group', 'role',)
    
admin.site.register(PrincipalRoleRelation, PrincipalRoleRelationAdmin)

