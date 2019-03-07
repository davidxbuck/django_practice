import operator

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    worddict = {}

    for word in wordlist:
        if word.strip(",.!?")[0].isalpha():
            if word.strip(",.!?") in worddict:
                worddict[word.strip(",.!?")] += 1
            else:
                worddict[word.strip(",.!?")] = 1

    wordlist = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'wordcount': len(wordlist), 'wordlist': wordlist})
