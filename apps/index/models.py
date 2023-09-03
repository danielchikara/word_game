from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    score = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.score
    

class SongsWord(models.Model):
    url_youtube = models.URLField(null=True, blank= True)
    name = models.CharField(max_length=150, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name
    
    def save(self):
        self.url_youtube = self.url_youtube.replace("watch?v=", "embed/")
        return super().save() 
    
class Word(models.Model):
    id_songs = models.ForeignKey(SongsWord,on_delete=models.CASCADE, null=True, blank=True)
    word = models.CharField(max_length=150)
    WORD_CHOICES = (
        ('G','Grave'),
        ('A','Aguda')
    )
    type_word = models.CharField(choices=WORD_CHOICES, max_length=1)
    order_b = models.IntegerField(null=True,blank=True)
    def __str__(self) :
        return self.word
