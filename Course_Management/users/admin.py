from django.contrib import admin

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ['user', 'user_name', 'DeptName', 'UserType']
    list_filter = ['UserType']

    def user_name(self, obj):
        return "%s %s" % (obj.user.first_name, obj.user.last_name)

    user_name.admin_order_field = 'user'


admin.site.register(Profile, ProfileAdmin)
