from contact.forms import ContactForms
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from contact.models import Contact

@login_required(login_url='contact:login')
def create(request):
    form_action = reverse('contact:create')

    if request.method == 'POST':
        form = ContactForms(request.POST,request.FILES)
        context = {
            'form': form,
            'site_title': 'Create - ',
            'form_action':form_action,
        }
        # condicao para que todo o formulario fr valido dai continua
        if form.is_valid():
            # retarda o salvamento na base de dados por conta do commit False
            contact = form.save(commit=False)
            contact.owner = request.user
            #contact.show = False
            # serve para salvaer na base de dados
            contact.save()
            # renderiza a pagina para update de forma dinamica
            return redirect('contact:update',contact_id=contact.pk)
        

        return render(
            request,
            'contact/create.html',
            context,
            
        )

    context = {
        'form': ContactForms(),
        'site_title': 'Create - ',
        'form_action':form_action,
    }

    return render(
        request,
        'contact/create.html',
    )

@login_required(login_url='contact:login')
def update(request,contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True, owner=request.user)
    form_action = reverse('contact:update',args=(contact_id,))

    if request.method == 'POST':
        form = ContactForms(request.POST,request.FILES,instance=contact)
        context = {
            'form': form,
            'site_title': 'Create - ',
            'form_action':form_action,
        }
        # condicao para que todo o formulario fr valido dai continua
        if form.is_valid():
            # retarda o salvamento na base de dados por conta do commit False
            contact = form.save()
            #contact.show = False
            # serve para salvaer na base de dados
            contact.save()
            # renderiza a pagina para update de forma dinamica
            return redirect('contact:update',contact_id=contact.pk)
        

        return render(
            request,
            'contact/create.html',
            context,
            
        )

    context = {
        'form': ContactForms(instance = contact),
        'site_title': 'Create - ',
        'form_action':form_action,
    }

    return render(
        request,
        'contact/create.html',
    )

@login_required(login_url='contact:login')
def delete(request,contact_id):

    contact = get_object_or_404(Contact, pk=contact_id, show=True, owner=request.user)
    
    confirmation = request.POST.get('confirmation','no')

    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')

    return render(
        request,
        'contact/contact.html',
        {
            'contact':contact,
            'confirmation':confirmation,
        }
    )