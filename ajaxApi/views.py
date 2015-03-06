from django.shortcuts import render,render_to_response,RequestContext,HttpResponse
from django.forms import Form
from mixer.models import Mixer
from jsonresponse import GenerateJSONFeeds,GenerateJSONPosts
"""
    Add feed to Mixer Objects and save to DB.
    Checks if feed is already added to DB.
    Checks if it's a valid URL.(need improved)
    :returns: Result of
              OK - on success
              Invalid URL - self explanatory
              Feed Already Exists - self explanatory
"""
def FeedAdd(feedurl):
    exists_num_rows =  Mixer.objects.filter(url = feedurl.lower()).count()
    if exists_num_rows > 0:
        #print "exists"
        return HttpResponse("Feed Already Exists!")
    else:
        if feedurl.lower().startswith('http://') or feedurl.lower().startswith('https://'):
            #print "adding ",feedurl
            p = Mixer(url=feedurl.lower())
            p.save()
        else:
            return HttpResponse("Invalid URL")
    return HttpResponse("OK")

"""
    Delete feed from Mixer Object by IDENTITY (ID)
    :returns: OK - on success
"""
def FeedDelete(request,id):
    print request.method
    if request.method == "GET" or request.method=="DELETE":
        Mixer.objects.get(id = id).delete()
        return HttpResponse("OK")

"""
    URL Landing
    Checks request if it is feeds or posts,
    :returns: JSON (feeds / posts) for GET Requests
              Result @FeedAdd for POST Request
"""
def AjaxAPI(request,action):
    if action == "feeds":
        if request.method=="POST":
            feedadd_result = FeedAdd(request.POST['url'])
            return HttpResponse(feedadd_result)
        if request.method=="GET":
            json_feeds = GenerateJSONFeeds()
            return HttpResponse(json_feeds)
    elif action == "posts":
          if request.method=="GET":
            json_posts = GenerateJSONPosts()
            return HttpResponse(json_posts)