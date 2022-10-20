from django.db import models

class items(models.Model):
    name=models.CharField(max_length=120)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    pImage=models.URLField()
