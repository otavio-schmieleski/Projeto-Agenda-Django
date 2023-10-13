from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404
from django.db.models import Q
from contact.models import Contact
from django.core.paginator import Paginator
# Create your views here.
# aqui configura a views principal

def index(request):
    # aqui utilizado o filter para selecionar apenas os contatos show=true e ordenar de forma descrecente
    contacts = Contact.objects.filter(show=True).order_by('-id') # aqui esta pegando todos os contatos do banco de dados

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos - '
    }

    return render(
        request,
        'contact/index.html',
        context
    )

def search(request):
    # pega o name do search,get para tentar pegar a variavel q e se nao tiver recebe nada e strip tira os espacos
    search_value = request.GET.get('q', '').strip()

    # checa se o usuario digitou algo, se nao digitou rediciona a pagina ao index
    if search_value == '':
        return redirect('contact:index')

    # aqui utilizado o filter para selecionar apenas os contatos show=true e ordenar de forma descrecente
                            # filtra pelo show       # utilizando o Q filtra pelo 1 e 2 nome todas as letras pesquisadas com icontains
    contacts = Contact.objects.filter(show=True) .filter(Q(first_name__icontains=search_value) | 
                                                        Q(last_name__icontains=search_value) |
                                                        Q(last_name__icontains=search_value) |
                                                        Q(phone__icontains=search_value) |
                                                        Q(email__icontains=search_value))\
        .order_by('-id') # aqui esta pegando todos os contatos do banco de dados

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Search - ',
        'search_valeu': search_value,
    }

    return render(
        request,
        'contact/index.html',
        context
    )


def contact(request,contact_id):
    # aqui utilizado o filter para selecionar apenas os contatos show=true e ordenar de forma descrecente
    single_contact = get_object_or_404(Contact,pk=contact_id,show=True)

    site_title = f'{single_contact.first_name} {single_contact.last_name} - '

    context = {
        'contact': single_contact,
        'site_title': site_title
    }

    return render(
        request,
        'contact/contact.html',
        context
    )
