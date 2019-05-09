from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request,'index.html')
def count(request):
    fulltext=request.GET['fulltext']

    wordlist= fulltext.split()

    worddict={}

    for word in wordlist:
        if word in worddict:
            #increase
            worddict[word]+=1
        else:
            #add to dictionary
            worddict[word] = 1
    sortedword=sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html',{'fulltext':fulltext, 'lenth':len(wordlist), 'sortedword':sortedword})

def aboutus(request):
    return render(request, 'aboutus.html')