from django.db import models

# Create your models here.
class List(models.Model):
    list_id = models.BigAutoField(primary_key=True)
    list_name= models.CharField(max_length=50)
    

    def __str__(self):
        return self.list_name