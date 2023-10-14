from django.urls import path
from contact import views
# cria um nome padrao para as urls da pagina 
app_name = 'contact'

urlpatterns = [
    # configura a url de pesquisa no campo search
    path('search/', views.search, name='search'),
    # configura a url da pagina principal
    path('', views.index, name='index'),

    # configura url do contato do  id passado por paramentro
    # contact (CRUD)
    path('contact/<int:contact_id>/detail/', views.contact, name='contact'),
    path('contact/create/', views.create, name='create'),
    path('contact/<int:contact_id>/update/', views.update, name='update'),
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),
    
    # User (CRUD)
    path('user/create/', views.register, name='register'),
    path('user/login/', views.login_view, name='login'),
    path('user/logout/', views.logout_view, name='logout'),
    path('user/update/', views.user_update, name='user_update'),









]