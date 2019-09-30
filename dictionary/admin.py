from django.contrib import admin
from .models import (
	Property,
	Category,
	Guarantee_Period,
	Property_unit,
	Period_term
)



admin.site.register(Property)
admin.site.register(Category)
admin.site.register(Guarantee_Period)
admin.site.register(Property_unit)
admin.site.register(Period_term)