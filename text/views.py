from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    dj_text = (request.POST.get('text', 'default'))

    removepunc = request.POST.get('removepunc', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

        analyzed = "" #initializing an empty string.

        for char in dj_text:
            if char not in punctuations:
                analyzed = analyzed + char
        
        params = {'purpose' : 'Remove Punctuations', 'analyzed_text' : analyzed}
        return render(request, 'analyze.html', params)

    elif(charcount == "on"):
        analyzed = len(dj_text)
        params = {'purpose' : 'Count Characters', 'analyzed_text' : analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")