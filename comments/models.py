from django.db import models
from instruments.models import Instrument


class Comment(models.Model):
    name = models.CharField(blank=True,max_length=100)
    text = models.TextField(blank=True)
    email = models.EmailField(blank=True,max_length=100)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    instruments = models.ForeignKey(Instrument, blank=True,null=True, related_name='instruments', on_delete=models.CASCADE)

    def __str__(self):
	    return "%s" %self.email

    class Meta:
	    verbose_name = 'Коментарии'
	    verbose_name_plural = 'Коментарии'