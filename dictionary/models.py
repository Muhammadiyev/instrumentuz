from django.db import models

class Property_unit(models.Model):
    power = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    rotation_frequency = models.CharField(max_length=100)

    def __str__(self):
	    return "%s" %self.power

class Property(models.Model):
    power = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    rotation_frequency = models.CharField(max_length=100)
    property_unit = models.ForeignKey(Property_unit,
            blank=True, null=True,
            related_name='property_of_property_unit',
            on_delete=models.CASCADE)

    def __str__(self):
	    return "%s" %self.power

    class Meta:
	    verbose_name = 'Характеристика'
	    verbose_name_plural = 'Характеристики'


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='user_img',blank=True)


    def __str__(self):
	    return "%s" %self.name
    
    # @property
    # def instruments(self):
    #     return self.instruments_of_category


    class Meta:
	    verbose_name = 'Категории'
	    verbose_name_plural = 'Категории'



class Guarantee_Period(models.Model):
    term = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    def __str__(self):
	    return "%s" %self.term

    class Meta:
	    verbose_name = 'Гарантийный срок'
	    verbose_name_plural = 'Гарантийный срок'


class Period_term(models.Model):
    term = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    def __str__(self):
	    return "%s" %self.term

    class Meta:
	    verbose_name = 'Срок скидки'
	    verbose_name_plural = 'Срок скидки'