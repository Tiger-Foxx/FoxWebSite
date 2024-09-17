from django.shortcuts import redirect, render
from FoxApp.models import *
from django.shortcuts import get_object_or_404
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
    } )


def post(request,id):
    template='FoxApp/page-blog-detail.html'
    post=get_object_or_404(Post,id=id)
    posts=Post.objects.all()[:3]

    return render(request,template_name=template,context={
        'post': post,
        'posts': posts,
    } )

def blog(request):
    template='FoxApp/blog.html'
    posts=Post.objects.all().order_by('-date')
    
    return render(request,template_name=template,context={
        'posts': posts,
    } )
    
def portfolio(request):
    template='FoxApp/page-portfolio.html'
    projets=Project.objects.all()
    posts=Post.objects.all()[:3]

    return render(request,template_name=template,context={
        'projets': projets,
        'posts':posts,
    } )
    
def projet(request,id):
    template='FoxApp/page-portfolio-detail.html'
    projet=get_object_or_404(Project,id=id)
    posts=Post.objects.all()[:3]
    return render(request,template_name=template,context={
        'projet': projet,
        'posts': posts,
    })

def subscribe(request):
    email=request.POST.get('email')
    try :
        visiteur=Visiteur.objects.create(email=email)
        visiteur.save()
        message=f'Merci ! {email} Vous recevrez nos nouvelles par email ! '
    except:
        message=f'Merci ! {email} mais vous recevez dejà nos nouvelles par email ! '
    return redirect('success',message=message)

def success(request, message='MERCI POUR VOTRE COOPERATION !'):
    template='FoxApp/page-success.html'
    return render(request,template_name=template,context={
        'message': message,
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
    return redirect('success',message=success)

