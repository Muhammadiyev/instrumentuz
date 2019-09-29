from django.contrib import admin
from .models import Image, Instrument, Instrument_in_Discount, Description





class InstrumentAdmin(admin.ModelAdmin):
	list_display = ['id','firm','name','price','categories','guarantee_period','property']
	readonly_fields = ('date',)

	class Meta:
		model = Instrument



admin.site.register(Instrument, InstrumentAdmin)

admin.site.register(Image)
admin.site.register(Description)
admin.site.register(Instrument_in_Discount)