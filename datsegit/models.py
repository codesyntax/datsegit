from django.db import models
from tinymce.models import HTMLField

class Edukia(models.Model):
    text = HTMLField()
    public = models.BooleanField(default=True)
    added = models.DateField(auto_now_add=True)

    
