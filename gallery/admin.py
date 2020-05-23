from django.contrib import admin
from .models import Category,Post,Location


# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Location)


# Other customizations
admin.AdminSite.site_header='Gallery'
