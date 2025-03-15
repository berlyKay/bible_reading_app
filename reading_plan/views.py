from django.http import JsonResponse
import requests
from datetime import datetime
from .services import fetch_audio
from reading_plan.models import BibleReading

def get_readings_by_date(request, date):
    try:
        readings = BibleReading.objects.filter(date=date).values("book", "chapter", "type")
        # print(readings)
        formatted_readings = list(readings)
        # print(formatted_readings)
        
        response_data = {
            "date": date,
            "readings": formatted_readings
            }
        print(response_data)  # This is the Python dictionary
        return JsonResponse(response_data)



        return JsonResponse({
            "date": date,
            "readings": formatted_readings
        })

    except BibleReading.DoesNotExist:
        return JsonResponse({"error": "No reading found for this date"}, status=404)


# def get_chapter_reading(request, book, chapter):
#     url = f"https://api.esv.org/v3/passage/text/?q={book}+1{chapter}"
#     headers = {
#         "x-rapidapi-host": "iq-bible.p.rapidapi.com",
#         "x-rapidapi-key": "1be48f3b0amsh89f3a6162da0e01p1f5bf0jsn8e82688afad6",
#     }
#     response = requests.get(url, headers=headers)

#     if response.status_code == 200:
#         data = response.json()
#         formatted_text = " ".join(f"{item['v']} {item['t']}" for item in data)

#         return JsonResponse(formatted_text)


    
def GetAudio(request):
    book_id = request.GET.get("bookId", 1)  
    chapter_id = request.GET.get("chapterId", 1)  
    version_id = request.GET.get("versionId", "kjv")  

    audio_url = fetch_audio(book_id, chapter_id, version_id)
    return JsonResponse({"fileName": audio_url})

    

def get_daily_proverb(request):
    today = datetime.today().day
    url = f"https://iq-bible.p.rapidapi.com/GetChapter?bookId=20&chapterId={today}&versionId=kjv"
    headers = {
        "x-rapidapi-host": "iq-bible.p.rapidapi.com",
        "x-rapidapi-key": "1be48f3b0amsh89f3a6162da0e01p1f5bf0jsn8e82688afad6",
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        formatted_text = " ".join(f"{item['v']} {item['t']}" for item in data)
        # print(formatted_text)

        return JsonResponse({"chapter": today, "text": formatted_text})

    return JsonResponse({"error": "Failed to fetch proverb"}, status=500)


def get_chapter_reading(request, book, chapter):
    print(book, chapter)

    url = f"https://api.esv.org/v3/passage/text/?q={book}+{chapter}"
    headers = {
        "Authorization": "Token d6ce5b1b49a0f64132ac5667312743e76964fbb1",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()

        chapter_title = data.get("canonical", "Unknown Title")
        passage_text = data.get("passages", ["No text found"])[0]

        passage_lines = passage_text.split("\n")
        footnotes = None
        for index, value in enumerate(passage_lines):
            if value == "Footnotes":
                x = index
                "\n".join(passage_lines[x:])
                cleaned_passage = "\n".join(passage_lines[3:x])
                break
        if footnotes is None:
            cleaned_passage = "\n".join(passage_lines[3:])

        passage_intro = passage_lines[2]

        formatted_data = {
            "title": chapter_title,
            "intro": passage_intro,
            "text": cleaned_passage,
        }

        if footnotes:
            formatted_data["footnotes"] = footnotes

        return JsonResponse(formatted_data)

def get_chapter(request):
    url = f"https://iq-bible.p.rapidapi.com/GetChapter?bookId=20&chapterId={today}&versionId=kjv"
    headers = {
        "x-rapidapi-host": "iq-bible.p.rapidapi.com",
        "x-rapidapi-key": "1be48f3b0amsh89f3a6162da0e01p1f5bf0jsn8e82688afad6",
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print(data)

        return JsonResponse(data)