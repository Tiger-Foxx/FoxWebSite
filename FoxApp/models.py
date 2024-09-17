from django.db import models

# Create your models here.

class Profile(models.Model):
    nom=models.CharField(max_length=328)
    sousTitre=models.TextField()
    photo=models.ImageField(upload_to='PhotoFox')
    descriptionP1=models.TextField()
    descriptionP2=models.TextField()
    signature=models.ImageField(upload_to='PhotoFox')
    email=models.EmailField()
    telephone=models.CharField(max_length=328)
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
        return f"PROJET | {self.nom.capitalize()} | {self.categorie.capitalize()}" 
    

class Post(models.Model):
    titre=models.CharField(max_length=328)
    description=models.TextField()
    photo500_x_800=models.ImageField(upload_to='PhotoFox',blank=True)
    photo800_x_533=models.ImageField(upload_to='PhotoFox',blank=True)
    categorie=models.CharField(max_length=328)
    auteur=models.CharField(max_length=328,blank=True)
    date=models.DateField(auto_now_add=True)
    contenuP1=models.TextField(blank=True,null=True)
    contenuConclusion=models.TextField(blank=True,null=True)
    contenuSitation=models.TextField(blank=True,null=True)


    def __str__(self):
        return f"ARTICLE | {self.titre.capitalize()} | {self.date}" 
    

class Visiteur(models.Model):
    email=models.EmailField()
    nom=models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return f"VISITEUR | {self.email}"

class Commentaire(models.Model):
    contenu=models.TextField()
    visiteur=models.ForeignKey(Visiteur,on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"COMMENTAIRE SUR | {self.post.titre} le {self.date}"

    

    
