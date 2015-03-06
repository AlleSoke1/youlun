import feedparser
from mixer.models import Mixer
from django.utils.html import escape


"""
    Method to escape an unicode string string
    :returns: Escaped string
"""
def escapeunicode(str):
    return str.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", '&#39;')


"""
    RSS Parsing function
    :returns: feedparser object output
"""
def ParseSingleRSSURL(URL):
    data = feedparser.parse(str(URL))
    return data

"""
    Parse all Feeds from MIXER
    :returns: JSON output with all feeds
"""
def ParseMixerRSS():
    Data = []
    for item in Mixer.objects.all():
        URL = item
        Data.append(ParseSingleRSSURL(URL))
    RSSData = []
    id=0
    for posts in Data:
        for post in posts.entries:
           #print post.title + " " + post.summary
            id+=1
            title = post.title.encode("utf-8")
            summary = post.summary.encode("utf-8")
            RSSData.append('{"id":'+str(id)+',"author":"-","title":"'+ str(escapeunicode(title)) +'","summary":"'+ str(escapeunicode(summary)) +'"}')
    return '{"response":{"status":"OK","result":['+','.join(RSSData)+']}}'