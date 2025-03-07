from django.http import JsonResponse
import requests
from datetime import datetime
from .services import fetch_random_proverb, fetch_text, fetch_audio
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
    
def get_random_proverb(request):
    verse_data = fetch_random_proverb()
    if 'error' in verse_data:
        return JsonResponse(verse_data, status=verse_data.get('status', 404))
    
    return JsonResponse(verse_data)

def GetAudio(request):
    book_id = request.GET.get("bookId", 1)  
    chapter_id = request.GET.get("chapterId", 1)  
    version_id = request.GET.get("versionId", "kjv")  

    audio_url = fetch_audio(book_id, chapter_id, version_id)
    return JsonResponse(audio_url)

def GetText(request):
    book_id = request.GET.get("bookId", 1)  
    chapter_id = request.GET.get("chapterId", 1)
    version_id = request.GET.get("versionId", "kjv") 

    text_url = fetch_text(book_id, chapter_id, version_id)
    return JsonResponse(text_url, safe=False)

def get_daily_proverb(request):
    today = datetime.today().day
    url = f"https://bible-api.com/proverbs+{today}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return JsonResponse({"chapter": today, "text": data.get("text", "No text found")})
    else:
        return JsonResponse({"error": "Failed to fetch chapter"}, status=response.status_code)

