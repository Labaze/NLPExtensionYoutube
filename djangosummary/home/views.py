import json
from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests as req
import re
from gensim.summarization import summarize


def index(request):
    return render(request, 'home/index.html')


@csrf_exempt
def results(request):
    # context = summarize_gensim(request)
    print(request.method)

    context = {}
    print(request.POST)
    if request.method == "POST":
        youtube_url = request.POST.get('url')
        print(youtube_url)
    end_url = re.findall('v=.*', youtube_url)
    youtube_caption_url = f'http://video.google.com/timedtext?lang=fr&{end_url[0]}'

    reponse = req.get(youtube_caption_url)

    soup = BeautifulSoup(reponse.content, 'html.parser')  # the parser that suits to the html
    text = soup.text.replace("\n", " ").replace("&quot", "").replace(".", ". ").replace("&#39;", "\'").replace("…",
                                                                                                               ". ").replace(
        "–", ". ").replace("?", "? ")

    context['resume'] = summarize(text, ratio=0.05)
    print(context['resume'])

    # return render(request, 'home/results.html',context)
    return HttpResponse(json.dumps({"resume": "%s" % context['resume']}, ensure_ascii=False).encode('utf8'),
                        content_type="application/json")

	# return JsonResponse({"resume": "%s" % context['resume']}, status=200)
