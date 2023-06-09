from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
class Picture(models.Model):
    OPTIONS_CATEGORY = [
        ("NEBULOSA", 'Nebulosa'),
        ("ESTRELA", 'Estrela'),
        ("GALÁXIA", 'Galáxia'),
        ("PLANETA", 'Planeta'),
   ]
    name = models.CharField(max_length=100, null=False, blank=False)
    legend = models.CharField(max_length=150, null=False, blank=False)
    category = models.CharField(max_length=100, choices=OPTIONS_CATEGORY, default='')
    description  = models.TextField(null=False, blank=False)
    src  = models.ImageField(upload_to='picture/%Y/%m/%d/', blank=True)
    published = models.BooleanField(default=False)
    date_picture = models.DateTimeField(default=datetime.now, blank=False)
    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user"
    )

    def __str__(self):
        return self.name

