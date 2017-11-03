from django.contrib import admin
from .models import Post



admin.site.site_header = 'Hello Team 36 User Login'


admin.site.register(Post)

