from django.db import models
from dictionary.models import *


class Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='user_img')

    def __str__(self):
	    return "%s" %self.name

    class Meta:
	    verbose_name = 'Изображении'
	    verbose_name_plural = 'Изображении'


class Instrument(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    guarantee_period = models.ForeignKey(Guarantee_Period, blank=True,null=True, related_name='instruments_of_guarantee_period', on_delete=models.CASCADE)
    image = models.ManyToManyField(Image, blank=True, related_name='images')
    categories = models.ForeignKey(Category, blank=True,null=True,related_name='instruments_of_category',on_delete=models.CASCADE)
    property = models.ForeignKey(Property, blank=True,null=True, related_name='property', on_delete=models.CASCADE)
    firm = models.ForeignKey('company.Firm', blank=True,null=True, related_name='instruments_of_firm', on_delete=models.CASCADE)

    def __str__(self):
	    return "%s" %self.name


        
    class Meta:
	    verbose_name = 'Инструмент'
	    verbose_name_plural = 'Инструменты'




class Instrument_in_Discount(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(max_length=100, blank=True,null=True)
    discount = models.IntegerField(default=0)
    discount_term = models.ForeignKey(Period_term, blank=True,null=True, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    instrument = models.ForeignKey(Instrument, blank=True,null=True, related_name='discount_of_instrument', on_delete=models.CASCADE)

    def __str__(self):
	    return "%s" %self.name

    class Meta:
	    verbose_name = 'Инструменты в скидке'
	    verbose_name_plural = 'Инструменты в скидке'




class Description(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    is_active = models.BooleanField(default=True)
    instrument = models.ForeignKey(Instrument, blank=True,null=True, related_name='description_of_instrument', on_delete=models.CASCADE)

    def __str__(self):
	    return "%s" %self.name

    class Meta:
	    verbose_name = 'Описание инструмента'
	    verbose_name_plural = 'Описание инструмента'
