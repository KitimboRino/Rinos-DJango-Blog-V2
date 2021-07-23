from django.contrib import admin
from .models import Post

# Register your models here.
# Allows blog pots to be accessibel in the admin area
admin.site.register(Post)