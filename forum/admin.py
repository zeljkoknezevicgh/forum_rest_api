from django.contrib import admin
from forum.models import Category, Post, Comment


admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
