Iniciar o projeto Django

python -m venv nome_do_venv
.\nome_do_venv\Scripts\Activate.ps1
pip install django
django-admin startproject project .
python manage.py startapp nome_do_app

# Configurar o git
git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main

# Configure o .gitignore
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT

# Migrando a base de dados do Django
 -- toda vez que atualizar o models executar os comando para atualizar o banco de dados -- 
python manage.py makemigrations
python manage.py migrate

# Para acessar o admin Django
python manage.py runserver
na barra de pesquisa coloca o ip/admin (http://127.0.0.1:8000/admin)

# Criando e modificando a senha de um super usuario Django
python manage.py createsuperuser

# Recuperar a senha do super usuario Django
python manage.py changepassword USERNAME

# Trabalhando com o model do Django

# Importe o módulo
from contact.models import Contact
# Cria um contato (Lazy)
# Retorna o contato
contact = Contact(**fields)
contact.save()
# Cria um contato (Não lazy)
# Retorna o contato
contact = Contact.objects.create(**fields)
# Seleciona um contato com id 10
# Retorna o contato
contact = Contact.objects.get(pk=10)
# Edita um contato
# Retorna o contato
contact.field_name1 = 'Novo valor 1'
contact.field_name2 = 'Novo valor 2'
contact.save()
# Apaga um contato
# Depende da base de dados, geralmente retorna o número
# de valores manipulados na base de dados
contact.delete()
# Seleciona todos os contatos ordenando por id DESC
# Retorna QuerySet[]
contacts = Contact.objects.all().order_by('-id')
# Seleciona contatos usando filtros
# Retorna QuerySet[]
contacts = Contact.objects.filter(**filters).order_by('-id')