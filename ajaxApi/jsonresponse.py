from django.core import serializers
from mixer.models import Mixer
from rssparser import ParseMixerRSS


"""
    Takes all objects from mixer (urls) and adds them to a JSON string
    :returns: JSON string with all mixer urls
"""
def GenerateJSONFeeds():
    MixerObjects = Mixer.objects.all()
    result=[]
    for url in Mixer.objects.all():
        result.append('{"id":'+str(url.id)+',"name":"'+str(url)+'"}')
    return '{"response":{"status":"OK","result":['+','.join(result)+']}}'

"""
    Calls @ParseMixerRSS
    :returns: JSON string from parsed RSS URL
"""
def GenerateJSONPosts():
    result = ParseMixerRSS()
    return result
