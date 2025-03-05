# from django.shortcuts import render
# import requests
# from django.urls import path
from django.http import JsonResponse
from .services import FetchAudo
from .services import FetchText
from reading_plan.models import ReadingPlan

def get_reading_by_date(request, date):
    try:
        reading = ReadingPlan.objects.get(date=date)
        book_name = reading.old_testament.split()[0]
        return JsonResponse({
            "date": reading.date,
            "old_testament": reading.old_testament,
            "new_testament": reading.new_testament,
            "psalm": reading.psalm,
            "book_name": book_name
        })
    except ReadingPlan.DoesNotExist:
        return JsonResponse({"error": "No reading found for this date"}, status=404)


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

