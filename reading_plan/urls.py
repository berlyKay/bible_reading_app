from django.urls import path
from .views import GetAudio, get_readings_by_date, get_daily_proverb, get_chapter_reading, get_chapter


urlpatterns = [
    path('readings/<str:book>/<int:chapter>/', get_chapter_reading, name="get_chapter_reading"),
    path('readings/<str:date>/', get_readings_by_date, name="get_reading_by_date"),
    path('chapter/', get_chapter, name="get_chapter"),
    path('audio/', GetAudio, name='get_audio'),
    path('proverb/', get_daily_proverb, name="get_daily_proverb"),

]
