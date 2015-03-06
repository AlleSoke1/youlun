from django.shortcuts import render,render_to_response,RequestContext,HttpResponse
from django.forms import Form
from mixer.models import Mixer
from jsonresponse import GenerateJSONFeeds,GenerateJSONPosts

def FeedAdd(feedurl):
    exists_num_rows =  Mixer.objects.filter(url = feedurl.lower()).count()
    if exists_num_rows > 0:
        print "exists"
        return HttpResponse("Feed Already Exists!")
    else:
        if feedurl.lower().startswith('http://') or feedurl.lower().startswith('https://'):
            print "adding ",feedurl
            p = Mixer(url=feedurl.lower())
            p.save()
        else:
            return HttpResponse("Invalid URL")
    return HttpResponse("OK")

def FeedDelete(request,id):
    print request.method
    if request.method == "GET" or request.method=="DELETE":
        Mixer.objects.get(id = id).delete()
        return HttpResponse("OK")


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