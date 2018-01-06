from django.contrib import admin
from .models import Writer, Movie, TvShow

admin.site.register(Writer)
admin.site.register(Movie)
admin.site.register(TvShow)
