from django.db import models

# Create your models here.
class User(models.Model):
    email  = models.EmailField(max_length=150)
    name = models.CharField(max_length= 150)
    txt = models.TextField(max_length=200)

    def __str__(self) -> str:
        return self.email
    

class SongsWord(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name
    
class Word(models.Model):
    id_songs = models.ForeignKey(SongsWord,on_delete=models.CASCADE, null=True, blank=True)
    word = models.CharField(max_length=150)
    WORD_CHOICES = (
        ('G','Grave'),
        ('A','Aguda')
    )
    type_word = models.CharField(choices=WORD_CHOICES, max_length=1)
    order_b = models.IntegerField()
    def __str__(self) :
        return self.word
