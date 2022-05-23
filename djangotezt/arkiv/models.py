from django.db import models

# Create your models here.

class Item(models.Model):
    item_physical_id = models.CharField(max_length=100)
    item_name = models.CharField(max_length=300)
    #pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.item_name
    