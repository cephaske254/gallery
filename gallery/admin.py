from django.contrib import admin
from .models import Category,Post,Location


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ('image_category', )

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Location)


# Other customizations
admin.AdminSite.site_header='Gallery'
