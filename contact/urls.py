from django.urls import path
from contact import Views
# cria um nome padrao para as urls da pagina 
app_name = 'contact'

urlpatterns = [
    # configura a url de pesquisa no campo search
    path('search/', Views.search, name='search'),
    # configura a url da pagina principal
    path('', Views.index, name='index'),

    # configura url do contato do  id passado por paramentro
    # contact (CRUD)
    path('contact/<int:contact_id>/detail/', Views.contact, name='contact'),
    path('contact/create/', Views.create, name='create'),
    path('contact/<int:contact_id>/update/', Views.update, name='update'),
    path('contact/<int:contact_id>/delete/', Views.delete, name='delete'),
    
    # User (CRUD)
    path('user/create/', Views.register, name='register'),
    path('user/login/', Views.login_view, name='login'),
    path('user/logout/', Views.logout_view, name='logout'),
    path('user/update/', Views.user_update, name='user_update'),









]