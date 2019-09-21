from django.contrib import admin
from .models import *

class InstrumentAdmin(admin.ModelAdmin):
	list_display = ['id','firm','name','price','categories','guarantee_period','property']


	class Meta:
		model = Instrument



admin.site.register(Instrument, InstrumentAdmin)

admin.site.register(Image)
admin.site.register(Description)
admin.site.register(Instrument_in_Discount)