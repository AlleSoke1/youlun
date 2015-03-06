from django.contrib import admin

# Register your models here.
from .models import Mixer
"""
    Class for Admin panel
"""
class MixerAdmin(admin.ModelAdmin):
    """
      Display ID and URL in Admin Panel
    """
    list_display = ["id","url"]

admin.site.register(Mixer,MixerAdmin)