#By Abhishek Sharma
#this is a sample o my django skill!

from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request, 'index.html')

def analyze(request):

    #get text
    djtext = request.POST.get('text', 'default')

    #check box values
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    #check which checkbox is on
    if removepunc == 'on':
        punctuations = '''!()-[];:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed


    if fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose':'Changed to UpperCase', 'analyzed_text':analyzed}
        djtext = analyzed

    if newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char!='\n' and char!='\r':
                analyzed = analyzed + char

        params = {'purpose': 'New lin remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if charcount == 'on':
        analyzed = len(djtext)

        params = {'purpose': 'Charecter Count', 'analyzed_text': analyzed}

    if (removepunc != 'on' and fullcaps != 'on' and newlineremover != 'on' and extraspaceremover != 'on' and charcount != 'on'):
        return HttpResponse("Error")


    return render(request, 'analyze.html', params)

