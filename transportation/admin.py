from django.contrib import admin
from .models import User,Role
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=("id","username","email","password")
    list_editable=("username","email","password")
class RoleAdmin(admin.ModelAdmin):
    list_display=("User_id","role_name")

admin.site.register(User,UserAdmin)
admin.site.register(Role,RoleAdmin)
