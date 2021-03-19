from django.db import models

# Create your models here.
class Post(models.Model):
    equipo = models.CharField(max_length=200)
    posicion = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    Reseña = models.TextField()

    def __str__(self):
        return self.equipo
