from django.db import models

# Create your models here.
"""
    Mixer Model
    :param: url - URL of RSS Feed
"""
class Mixer(models.Model):
    url = models.TextField(max_length=150,blank=False,null=True)

    def __unicode__(self):
        return self.url


