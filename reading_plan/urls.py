from django.urls import path, include
from .views import GetAudio
from .views import GetText

urlpatterns = [
    path('audio/', GetAudio, name='get_bible_chapter'),
    path('text/', GetText, name='get_bible_chapter'),
]
