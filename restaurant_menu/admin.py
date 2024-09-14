from django.contrib import admin
from .models import Item

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("meal", "status", "meal_type", )
    list_filter = ("status", )
    search_fields = ("meals", "description",)


admin.site.register(Item, MenuItemAdmin)

# to create an admin login we have to go to the django project and want to run python manage.py createsuperuser
# it will then ask you to create a username and then a password for now i have created using
# username rishilshah and password as Asdfghjkl@13123

# The name Items comes from the models.py



