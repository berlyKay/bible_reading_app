import requests

def fetch_bible_chapter(book_id, chapter_id, version_id):
    url = "https://iq-bible.p.rapidapi.com/GetChapter"
    headers = {
        "x-rapidapi-host": "iq-bible.p.rapidapi.com",
        "x-rapidapi-key": "your-api-key-here",
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
