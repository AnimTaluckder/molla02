from django.db import models

# Create your models here.
class Product(models.Model):
     p_name  = models.CharField(max_length=50)
     p_image = models.ImageField(upload_to="my_infoimage")
     p_det   = models.TextField()
class Slider(models.Model):
     s_image   = models.ImageField(upload_to="my_infoimage")
     s_heading = models.CharField(max_length=50)
     s_det     = models.TextField()      

