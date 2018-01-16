from django.db import models
from django.utils import timezone

class Galeria(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
class Lekarz(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    #CHIRURG = 'CH'
    #NEUROCHIRURG = 'NC'
    #KARDIOLOG = 'KG'
    #ANESTEZJOLOG = 'AN'
    #ENDOKRYNOLOG = 'EN'
    CHIRURG = 'Chirurg'
    NEUROCHIRURG = 'Neurochirurg'
    KARDIOLOG = 'Kardiolog'
    ANESTEZJOLOG = 'Anestezjolog'
    ENDOKRYNOLOG = 'Endokrynolog'
    SPECJALIZACJA_CHOICES = (
        (CHIRURG, 'Chirurg'),
        (NEUROCHIRURG, 'Neurochirurg'),
        (KARDIOLOG, 'Kardiolog'),
        (ANESTEZJOLOG, 'Anestezjolog'),
        (ENDOKRYNOLOG, 'Endokrynolog'),
    )
    specjalizacja = models.CharField(max_length=20,
                                     choices=SPECJALIZACJA_CHOICES,
                                     default=CHIRURG)
    nazwisko = models.CharField(max_length=20)
    imię = models.CharField(max_length=20)
    cena = models.CharField(max_length=3)
    opis = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nazwisko

    def __str__(self):
        return self.specjalizacja

    def is_upperclass(self):
        return self.specjalizacja in (self.ANESTEZJOLOG, self.ENDOKRYNOLOG)