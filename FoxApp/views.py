from django.shortcuts import render

# Create your views here.

def index(request):
    template='FoxApp/index.html'
    return render(request,template_name=template )
