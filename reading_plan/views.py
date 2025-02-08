# from django.shortcuts import render
# import requests
# from django.urls import path
from django.http import JsonResponse
from .services import FetchAudo
from .services import FetchText


def GetAudio(request):
    book_id = request.GET.get("bookId", 1)  
    chapter_id = request.GET.get("chapterId", 1)  
    version_id = request.GET.get("versionId", "kjv")  

    audio_url = FetchAudo(book_id, chapter_id, version_id)
    return JsonResponse(audio_url)

def GetText(request):
    book_id = request.GET.get("bookId", 1)  
    chapter_id = request.GET.get("chapterId", 1)
    version_id = request.GET.get("versionId", "kjv") 

    text_url = FetchText(book_id, chapter_id, version_id)
    print("DEBUG:", type(text_url), text_url)
    return JsonResponse(text_url, safe=False)

