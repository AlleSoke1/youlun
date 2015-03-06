from django.db import models

# Create your models here.

class Mixer(models.Model):
    url = models.TextField(max_length=150,blank=False,null=True)
    #addDate = models.DateTimeField(auto_now=False,auto_now_add=True)


    def __unicode__(self):
        return self.url


