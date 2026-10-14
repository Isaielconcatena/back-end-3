from django.db import models

# Create your models here.
class Student(models.Model): # O el nombre de entidad que uses en tu proyecto
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    imagen = models.ImageField(upload_to='estudiantes/', null=True, blank=True)

    def __str__(self):
        return str(self.id) + " " + self.name + " (SCORE: " + str(self.score) + ")"
