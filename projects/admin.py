from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Project

@admin.register(Project)
class ProjectAdmin(MarkdownxModelAdmin):
    list_display = ('name',)
    fields = ['name', 'description', 'video_link']
