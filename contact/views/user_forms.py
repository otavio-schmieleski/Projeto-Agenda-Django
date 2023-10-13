from django.shortcuts import render,redirect
from contact.forms import RegisterForm,RegisterUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages,auth

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'Usuário registrado')
            # exibi uma mensagem na tela
            return redirect('contact:login')

    return render(
        request,
        'contact/register.html',
        {
            'form':form
        }
    )

def login_view(request):
    # formulario de autenticacao do django
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request,data = request.POST)

        if form.is_valid():
            # seleciona o ususario
            user = form.get_user()
            messages.success(request,'Logado com sucesso!!')
            # para entra com um usario na pagina com o django 
            auth.login(request, user)
            return redirect('contact:index')
        messages.error(request,'Login Invalido!')

    return render(
        request,
        'contact/login.html',
        {
            'form':form
        }
        
    )

@login_required(login_url='contact:login')
def logout_view(request):
    # desloga o usuario
    auth.logout(request)
    # rediciona a pagina para login
    return redirect('contact:login')


# faz com que o usuario tenha que estar logado para acessar esta informacao
@login_required(login_url='contact:login')
def user_update(request):
    # aqui passa a instance para completar os campos do formulario automaticamente
    form = RegisterUpdateForm(instance=request.user)
    if request.method != 'POST':
        return render(
            request,
            'contact/user_update.html',
            {
                'form':form
            }
        )
    
    form = RegisterUpdateForm(data=request.POST ,instance=request.user)

    if not form.is_valid():
        return render(
            request,
            'contact/user_update.html',
            {
                'form':form
            }
        )
    
    form.save()

    return redirect('contact:user_update')