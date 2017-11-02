from django.contrib import admin
from .models import Post


admin.site.site_header = 'User Login Page'

admin.site.register(Post)
