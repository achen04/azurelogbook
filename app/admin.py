from django.contrib import admin
from .models import Post


admin.site.site_header = 'My User'

admin.site.register(Post)
