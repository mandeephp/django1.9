from django.contrib import admin
from app.models import *
from django.contrib.sites.models import Site
# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
	list_display = ['Title', 'Timestamp', 'Updated']
	list_display_link = ['Content']
	list_filter = ['Timestamp', 'Updated']
	search_field = ['Content']
	class Meta:
		model = Post

admin.site.register(Post, PostModelAdmin)
admin.site.unregister(Site)
