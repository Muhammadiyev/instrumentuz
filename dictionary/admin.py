from django.contrib import admin
from .models import *

class PropertyAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Property._meta.fields]
	class Meta:
		model = Property

admin.site.register(Property, PropertyAdmin)


class CategoryAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Category._meta.fields]
	class Meta:
		model = Category

admin.site.register(Category, CategoryAdmin)
admin.site.register(Guarantee_Period)
admin.site.register(Period_term)