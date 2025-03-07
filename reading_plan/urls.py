from django.urls import path
from .views import GetAudio, GetText, get_reading_by_date, get_daily_proverb


urlpatterns = [
    # path('api/random-proverb/', get_random_proverb, name="get_random_proverb"),
    path('proverb/', get_daily_proverb, name="get_daily_proverb"),
    path('audio/', GetAudio, name='get_bible_chapter'),
    path('text/', GetText, name='get_bible_chapter'),
    path('reading/<str:date>/', get_reading_by_date, name="get_reading_by_date"),
]
