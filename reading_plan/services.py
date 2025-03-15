import requests
import random
from django.http import JsonResponse

# def fetch_random_proverb():
#     url = "https://bible-api.com/proverbs+1"
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()
#         return JsonResponse({"chapter": data.get("text", "No text found")})
#     else:
#         return JsonResponse({"error": "Failed to fetch chapter"}, status=response.status_code)
    


def fetch_audio(book_id, chapter_id, version_id):
    url = "https://iq-bible.p.rapidapi.com/GetAudioNarration?bookId=20&chapterId=01&versionId=kjv"
    headers = {
        "x-rapidapi-host": "iq-bible.p.rapidapi.com",
        "x-rapidapi-key": "1be48f3b0amsh89f3a6162da0e01p1f5bf0jsn8e82688afad6",
    }
    params = {
        "bookId": book_id,
        "chapterId": chapter_id,
        "versionId": version_id,
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()  
    else:
        return {"error": f"API request failed with status code {response.status_code}"}

# def fetch_text(book_id, chapter_id, version_id):
#     url = "https://iq-bible.p.rapidapi.com/GetBookAndChapterNameByBookAndChapterId?bookAndChapterId=01001&language=english"
#     headers = {
#         "x-rapidapi-host": "iq-bible.p.rapidapi.com",
#         "x-rapidapi-key": "1be48f3b0amsh89f3a6162da0e01p1f5bf0jsn8e82688afad6",
#     }
#     params = {
#         "bookId": book_id,
#         "chapterId": chapter_id,
#         "versionId": version_id,
#     }

#     response = requests.get(url, headers=headers, params=params)

#     if response.status_code == 200:
#         return response.json()  # Returns the chapter data
#     else:
#         return {"error": f"API request failed with status code {response.status_code}"}