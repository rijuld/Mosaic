from django.contrib import admin
from .models import posts,comments,following,Todo_likes

# Register your models here.

admin.site.register(posts)
admin.site.register(comments)
admin.site.register(following)
admin.site.register(Todo_likes)