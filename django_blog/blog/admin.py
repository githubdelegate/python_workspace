from django.contrib import admin

from .models import Post,Category,Tag
# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','created_time','modified_time','category','author']

    