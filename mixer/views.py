from django.shortcuts import render,render_to_response,RequestContext

from .models import Mixer
# Create your views here.
"""
    Mixer View , renders homepage
"""
def MixerView(request):

    context = RequestContext(request)
    mixerObjects = Mixer.objects.order_by('id') #order ascending by id
    mixer_dict = {'mixerDict': mixerObjects,'count': Mixer.objects.count()}

    return render_to_response('home.html',mixer_dict,context)