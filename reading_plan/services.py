import requests

def FetchAudo(book_id, chapter_id, version_id):
    url = "https://iq-bible.p.rapidapi.com/GetAudioNarration?bookId=01&chapterId=02&versionId=kjv"
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
        return response.json()  # Returns the chapter data
    else:
        return {"error": f"API request failed with status code {response.status_code}"}

def FetchText(book_id, chapter_id, version_id):
    url = "https://iq-bible.p.rapidapi.com/GetBookAndChapterNameByBookAndChapterId?bookAndChapterId=01001&language=english"
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
        return response.json()  # Returns the chapter data
    else:
        return {"error": f"API request failed with status code {response.status_code}"}