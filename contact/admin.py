from django.contrib import admin
from contact import models
# Register your models here.

# configurando o models criado no admin do Django
@admin.register(models.Contact)
class ContatcAdmin(admin.ModelAdmin):
    # serve para colocar titulos e conteudo no cabecalho de visualizacao do admin
    list_display ='id','first_name','last_name','phone','show',

    # ordena pelo id em ordem descrecente ou se colocar 'id' em ordem crescente
    ordering = '-id',

    #serve para criar um filtro ao lado para pesquisa
    #list_filter = 'created_date',

    # campo de pesquisa, e passa os parametro que podem ser pesquisados
    search_fields = 'id','first_name','last_name',

    # configura a quantidade de itens para mostrar na mesma pagina
    list_per_page = 50  #neste exemplo so sera exibido na tela os primeiros 50 contatos o resto fica em outras paginas

    # configura o maximo de contato que pode ser exibido quando clicado no mostrar tudo
    list_max_show_all = 500

    # editar os valores sem precisar abri-los e passa os campos que podem ser editados
    list_editable = 'first_name', 'last_name', 'show',

    #colocar o link de direcionamento em outra partes do models
    list_display_links = 'id','phone', # quando clicado no id ou phone vai carregar o link


# configurando o models criado no admin do Django
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    # serve para colocar titulos e conteudo no cabecalho de visualizacao do admin
    list_display ='name',

    # ordena pelo id em ordem descrecente ou se colocar 'id' em ordem crescente
    ordering = '-id',
