from django.db import models

# Create your models here.

class Profile(models.Model):
    nom=models.CharField(max_length=328)
    sousTitre=models.TextField()
    photo=models.ImageField(upload_to='PhotoFox')
    descriptionP1=models.TextField()
    descriptionP2=models.TextField()
    signature=models.ImageField(upload_to='PhotoFox')
    cv=models.FileField(upload_to='FilesFox',blank=True,null=True)

    def __str__(self):
        return f"MON PROFILE | {self.nom.capitalize()}" 
    

class Project(models.Model):
    nom=models.CharField(max_length=328)
    description=models.TextField()
    photo1=models.ImageField(upload_to='PhotoFox',blank=True)
    photo2=models.ImageField(upload_to='PhotoFox',blank=True)
    photo3=models.ImageField(upload_to='PhotoFox',blank=True)
    categorie=models.CharField(max_length=328)
    sujet=models.CharField(max_length=328,blank=True)
    date=models.DateField(blank=True)
    demo=models.URLField(blank=True)
    signature=models.ImageField(upload_to='PhotoFox')
    cv=models.FileField(upload_to='FilesFox')

    def __str__(self):
        return f"MON PROFILE | {self.nom.capitalize()}" 