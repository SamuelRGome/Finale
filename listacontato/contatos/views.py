from django.shortcuts import render, redirect 
from .models import Contato

# Create your views here.
def index(request):
    contatos = Contato.objects.all()
    return render(request, 'index.html',{'contatos': contatos})

def addContact(request):
    if request.method == 'POST':
        novo_contato = Contato(
            nome_completo = request.POST['fullname'],
            relacao = request.POST['relationship'],
            email = request.POST['email'],
            numero = request.POST['phone-number'],
            endereco = request.POST['address'],
        )
        novo_contato.save()
        return redirect('/')
    return render(request, 'new.html')