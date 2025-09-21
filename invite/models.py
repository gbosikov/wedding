from django.db import models

# Create your models here.
from django.db import models

class RSVP(models.Model):
    YES = 'yes'
    NO = 'no'
    ATTEND_CHOICES = [(YES, 'Yes'), (NO, 'No')]

    name = models.CharField(max_length=200)
    attendance = models.CharField(max_length=3, choices=ATTEND_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} ({self.attendance})'
