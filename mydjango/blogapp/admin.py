import imp
from django.contrib import admin

# Register your models here.
from . models import Post

@admin.register(Post)
class BookmarkAdmim(admin.ModelAdmin):
    list_display= ('id', 'title')