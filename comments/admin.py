from django.contrib import admin
from .models import *

class CommentAdmin(admin.ModelAdmin):
	list_display = ['name','email','text','date', 'instruments']

	class Meta:
		model = Comment

admin.site.register(Comment, CommentAdmin)
