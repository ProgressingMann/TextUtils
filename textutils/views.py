# Created by me
from django.http import HttpResponse
from django.shortcuts import render
import re
import string


def analyzetext(request):
    return render(request, 'bootstrap/AnalyzeTextForm.html')


def analyzedtext(request):
    # print(text)
    text = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    toupper = request.POST.get('toupper', 'off')
    deletespace = request.POST.get('deletespace', 'off')
    removeline = request.POST.get('removeline', 'off')
    # print(text)
    # print(removepunc, toupper, deletespace, removeline)
    analyzed = ''
    if removepunc == 'on':
        text = removepuncs(text)
    if toupper == 'on':
        text = capitalize(text)
    if deletespace == 'on':
        text = removeextraspace(text)
    if removeline == 'on':
        text = removelines(text)
    # print(text)
    if text != 'default':
        return render(request, 'bootstrap/Analyzed.html', {'analyzed_text': text})
    else:
        return HttpResponse("You did not enter any text..")


def removepuncs(text):
    puncs = string.punctuation
    no_puncs = re.compile('[' + puncs + ']+')
    analyzed_text = no_puncs.sub('', text)
    return analyzed_text

def capitalize(text):
    return text.upper()

def removeextraspace(text):
    return re.compile('\s+').sub(' ', text)

def removelines(text):
    return re.compile('\n|\r').sub('', text)