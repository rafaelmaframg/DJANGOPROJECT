from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:receita_id>', views.receita, name='receita'),
    path('buscar', views.buscar, name='buscar'),
    path('cria/receita', views.cria_receita, name='cria_receita'),
    path('deleta/<int:receita_id>', views.deleta_receita, name='deleta_receita'),
    path('editar/<int:receita_id>', views.editar_receita, name='editar_receita'),
    path('atualiza_receita', views.atualiza_receita, name='atualiza_receita')
]