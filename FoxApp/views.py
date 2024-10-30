from django.shortcuts import redirect, render
from markdown_it.rules_inline import image

from FoxApp.models import *
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Visiteur, Annonce

# Create your views here.

def index(request):
    template='FoxApp/index.html'
    projets= Project.objects.all()
    posts=Post.objects.all()[:3]
    profile=Profile.objects.all()[0]
    
    return render(request,template_name=template,context={
        'projets': projets,
        'posts': posts,
        'profile': profile,
        'index':True,
    } )


def post(request,id):
    template='FoxApp/page-blog-detail.html'
    post=get_object_or_404(Post,id=id)
    posts=Post.objects.all()[:3]
    profile=Profile.objects.all()[0]
    commentaires=Commentaire.objects.filter(post=post)


    return render(request,template_name=template,context={
        'post': post,
        'posts': posts,
        'profile': profile,
        'commentaires': commentaires,
    } )

def blog(request):
    template='FoxApp/page-blog.html'
    posts=Post.objects.all().order_by('-date')
    paginator=Paginator(posts,6)
    page=request.GET.get('page')
    posts_page=paginator.get_page(page)
    recents=Post.objects.all()[:3]
    profile=Profile.objects.all()[0]


    return render(request,template_name=template,context={
        'posts_page': posts_page,
        'recents':recents,
        'profile': profile,

    } )
    
def portfolio(request):
    template='FoxApp/page-portfolio.html'
    projets=Project.objects.all()
    posts=Post.objects.all()[:3]
    profile=Profile.objects.all()[0]

    return render(request,template_name=template,context={
        'projets': projets,
        'posts':posts,
        'profile': profile,
    } )
    
def projet(request,id):
    template='FoxApp/page-portfolio-detail.html'
    projet=get_object_or_404(Project,id=id)
    posts=Post.objects.all()[:3]
    profile=Profile.objects.all()[0]
    return render(request,template_name=template,context={
        'projet': projet,
        'posts': posts,
        'profile': profile,
    })

def subscribe(request):
    email=request.POST.get('email')
    try :
        visiteur=Visiteur.objects.create(email=email)
        visiteur.save()
        message=f'Merci ! {email} Vous recevrez nos nouvelles par email ! '
        envoyer_email(message='Merci de votre visite  ! vous recevrez toutes les dernières NEWS Tech de FOX , BISOU',email=email,sujet='BIENVENUE CHEZ FOX !!!')
    except:
        message=f'Merci ! {email} mais vous recevez dejà nos nouvelles par email ! '
    return redirect('success',message=message)

def success(request, message='MERCI POUR VOTRE COOPERATION !'):
    template='FoxApp/page-success.html'
    profile=Profile.objects.all()[0]

    return render(request,template_name=template,context={
        'message': message,
        'profile': profile,
    })
    
def comment(request,id):
    email=request.POST.get('email')
    nom=request.POST.get('nom')
    contenu=request.POST.get('contenu')
    try:
        
        visiteur=Visiteur.objects.create(email=email,nom=nom)
        visiteur.save()
    except:
        visiteur=Visiteur.objects.get(email=email)[0]
    post=get_object_or_404(Post,id=id)
    commentaire=Commentaire.objects.create(visiteur=visiteur,contenu=contenu,post=post)
    commentaire.save()
    return redirect('post', id=id)

def sendMessage(request):
    nom=request.POST.get('nom')
    email=request.POST.get('email')
    contenu=request.POST.get('contenu')
    objet=request.POST.get('objet')
    success=f'MERCI {nom} POUR VOTRE MESSAGE !'
    try:
        visiteur=Visiteur.objects.create(email=email,nom=nom)
        visiteur.save()
    except:
        visiteur=Visiteur.objects.get(email=email)
        visiteur.nom=nom
        visiteur.save()
    message=Message.objects.create(visiteur=visiteur,objet=objet,contenu=contenu)
    message.save()
    envoyer_email(message=contenu,sujet='NOUVEAU MESSAGE SUR LE SITE FOX',email='donfackarthur750@gmail.com')
    return redirect('success',message=success)





def sendmail(request):
    template = 'FoxApp/page-sendmail.html'

    if not request.user.is_superuser:
        return redirect('index')

    if request.method == 'POST':
        contenuP1 = request.POST.get('contenuP1')
        contenuConclusion = request.POST.get('contenuConclusion')
        contenuSitation = request.POST.get('contenuSitation')
        image=request.POST.get('contenuImage')

        annonce = Annonce.objects.create(
            contenuP1=contenuP1,
            contenuConclusion=contenuConclusion,
            contenuSitation=contenuSitation
        )

        sujet = f"NOUVELLE ANNONCE DE FOX , TON RENARD PREF HAHA !"

        # Construire le contenu HTML de l'email
        message_html = f"""
        <html>
            <body>
                <h2> hey ! Nouvelle Annonce de FOX</h2>
                <p> <strong>{annonce.contenuP1}</strong></p>
                <blockquote>{annonce.contenuSitation}</blockquote>
                <p><b>{annonce.contenuConclusion}</b></p>
                <img src="{image}">
            </body>
        </html>
        """

        # Envoi de l'email HTML à tous les visiteurs
        visiteurs = Visiteur.objects.all()
        for visiteur in visiteurs:
            envoyer_email_html(visiteur.email, sujet, message_html)

        return redirect('success',message='Annonce Publiée !!')

    return render(request, template)



# Fonction pour envoyer un email en HTML
def envoyer_email_html(email, sujet, message_html):
    try:
        send_mail(
            sujet,
            "",  # Le message texte peut être laissé vide si on utilise uniquement HTML
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
            html_message=message_html  # Contenu HTML
        )
        print(f"Email HTML envoyé avec succès à {email}")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email à {email}: {e}")


def envoyer_email_aux_visiteurs(sujet, message):
    # Récupérer tous les emails des visiteurs
    visiteurs = Visiteur.objects.all()

    # Pour chaque visiteur, on envoie un email individuel
    for visiteur in visiteurs:
        envoyer_email(visiteur.email, sujet, message)


def envoyer_email(email, sujet, message):
    # Envoyer l'email
    try:
        send_mail(
            sujet,
            message,
            settings.EMAIL_HOST_USER,  # Expéditeur
            [email],  # Destinataire
            fail_silently=False,
        )
        print(f"Email envoyé avec succès à {email}")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email à {email}: {e}")

