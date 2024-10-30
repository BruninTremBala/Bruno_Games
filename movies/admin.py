from django.contrib import admin

from .models import Post, Review, List, Provider

admin.site.register(Post)
admin.site.register(Review)
admin.site.register(List)
admin.site.register(Provider)
