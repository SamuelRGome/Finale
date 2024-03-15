from django.shortcuts import render, redirect 
from .models import Contato

# Create your views here.
def index(request):
    contatos = Contato.objects.all()
    busca_input = request.GET.get('search-area')
    if busca_input:
        contatos = Contato.objects.filter(nome_completo__icontains=busca_input)
    else:
        contato = Contato.objects.all()
        busca_input = ''
    return render(request, 'index.html',{'contatos': contatos, 'busca_input': busca_input})

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

def contactProfile(request, pk):
    contact = Contato.objects.get(id=pk)
    return render(request, 'contact-profile.html', {'contact': contact})

def editContact(request, pk):
    contact = Contato.objects.get(id=pk) 

    if request.method == 'POST':
        contact.nome_completo = request.POST['fullname']
        contact.relacao = request.POST['relationship']
        contact.email = request.POST['e-mail']
        contact.numero = request.POST['phone-number']
        contact.endereco = request.POST['address']
        contact.save()
        return redirect('/profile/' + str(contact.id))
    return render(request, 'edit.html' , {'contact': contact})

def deleteContact(request, pk):
    contact = Contato.objects.get(id=pk)

    if request.method == 'POST':
        contact.delete()
        return redirect('/')
    return render(request, 'delete.html', {'contact': contact})