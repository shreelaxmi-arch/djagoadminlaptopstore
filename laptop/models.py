from django.db import models

# Create your models here.
class Laptop(models.Model):
    name=models.CharField(max_length=100)
    model=models.CharField(max_length=100)
    price=models.IntegerField()
    description=models.TextField()
    image=models.ImageField()
    def __str__(self):
        result=self.name
        return result
    class Meta:
        db_table="laptops"
