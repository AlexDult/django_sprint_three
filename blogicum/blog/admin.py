from django.contrib import admin
from .models import Category, Location, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'slug',
        'is_published',
        'created_at'
    )

    # list_editable = (
    #     'description',
    #     'slug',
    #     'is_published'
    # )
    list_display_links = ('title',)

admin.site.register(Category, CategoryAdmin)


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_published'
    )

    list_editable = (

        'is_published',
    )


admin.site.register(Location, LocationAdmin)
# # Register your models here.
#
#
class PostAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'is_published'
    )

    list_editable = (

        'is_published',
    )


admin.site.register(Post, PostAdmin)

