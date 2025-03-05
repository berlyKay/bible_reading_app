from django.urls import path
from .views import GetAudio
from .views import GetText
from .views import get_reading_by_date


urlpatterns = [
    path('audio/', GetAudio, name='get_bible_chapter'),
    path('text/', GetText, name='get_bible_chapter'),
    path("reading/<str:date>/", get_reading_by_date, name="get_reading_by_date"),
]
