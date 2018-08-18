from django.db import models

# Create your models here.
POSITIVO="POS"
NEGATIVO="NEG"
NEUTRO="NEU"

COMENTS =(
	(POSITIVO,'+'),
	(NEGATIVO,'-'),
	(NEUTRO,'N')
)

class Candidato(models.Model):
	nombre = models.CharField(max_length=150)
	partidoPolitico =models.CharField(max_length=150)
	web=models.URLField()
	descripcion =models.TextField(blank=True, null=True, default="")
	created_at=models.DateTimeField(auto_now_add=True) #Cada ves que se created_at
	modified_at=models.DateTimeField(auto_now=True) #cada vez que se actuliza
	Comentario=models.CharField(max_length=10, choices=COMENTS)
	