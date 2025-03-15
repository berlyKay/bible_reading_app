from django.db import models

class BibleReading(models.Model):
    date = models.DateField()
    book = models.CharField(max_length=255, null=True)  # e.g., "Genesis", "Matthew", "Psalm"
    chapter = models.CharField(max_length=50, null=True)  # Keeping it a CharField for flexibility, e.g., "Your choice"
    type = models.CharField(max_length=50, choices=[
        ('Old Testament', 'Old Testament'),
        ('New Testament', 'New Testament'),
        ('Psalm', 'Psalm'),
    ], null=True)

    def __str__(self):
        return f"{self.date}: {self.type} - {self.book} {self.chapter}"
    
    class Meta:
        db_table = 'bible_readings'


# class BibleReading(models.Model):
#     date = models.DateField(unique=True)
#     old_testament_reading = models.CharField(max_length=255, help_text="e.g., Genesis 1, Genesis 2")
#     new_testament_reading = models.CharField(max_length=255, help_text="e.g., Matthew 1")
#     psalm_reading = models.CharField(max_length=255, default="Your choice", help_text="Psalm reading for the day.")

#     def __str__(self):
#         return f"{self.date}: OT - {self.old_testament_reading}, NT - {self.new_testament_reading}, Psalm - {self.psalm_reading}"


# from django.db import models

# # Create your models here.
# class ReadingPlan(models.Model):
    
#     date = models.DateField()

#     ot_book = models.CharField(max_length=100, blank=True, null=True)
#     ot_chapter = models.IntegerField(blank=True, null=True)

#     nt_book = models.CharField(max_length=100, blank=True, null=True)
#     nt_chapter = models.IntegerField(blank=True, null=True)

#     psalm_book = models.CharField(max_length=100, blank=True, null=True, default="Psalm of choice")
#     psalm_chapter = models.IntegerField(blank=True, null=True)

#     def __str__(self):
#         return f"ReadingPlan for {self.date}"

# from django.http import JsonResponse
# from .api_request import fetch_bible_chapter  # Assuming fetch_bible_chapter is in services.py


