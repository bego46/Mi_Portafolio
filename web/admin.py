from django.contrib import admin
from .models import Proyecto, BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_publicacion')

admin.site.register(Proyecto)
