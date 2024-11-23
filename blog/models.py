from django.conf import settings
from django.db import models
from django.utils import timezone

# class es una palabra clave que indica que estamos definiendo un objeto
# Post es el nombre de nuestro modelo (Evita espacios y caracteres especiales). Siempre inicia el nombre de una clase con una letra mayúscula.
# models.Model significa que Post es un modelo de Django, así Django sabe que debe guardarlo en la base de datos.

class Post(models.Model): # esta línea define nuestro modelo (es un objeto)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # ForeignKey este es una relación (link) con otro modelo
    title = models.CharField(max_length=200) # así es como defines un texto con un número limitado de caracteres.
    text = models.TextField() # este es para texto largo sin límite.
    created_date = models.DateTimeField( # este es fecha y hora.
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
