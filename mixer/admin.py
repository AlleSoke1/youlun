from django.contrib import admin

# Register your models here.
from .models import Mixer

class MixerAdmin(admin.ModelAdmin):
    """
      Display URL in Admin Panel
    """
    list_display = ["id","url"]

admin.site.register(Mixer,MixerAdmin)