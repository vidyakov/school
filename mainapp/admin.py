from django.contrib import admin

from .models import Course, Tag, Author


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = 'name', 'author', 'price'
    list_display_links = list_display


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = 'name',
    list_display_links = list_display


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = 'first_name',
    list_display_links = list_display
