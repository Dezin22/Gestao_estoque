from django.urls import path

from . import views

app_name = 'cadastro'
urlpatterns = [
    path('',views.index, name='index'),
    path('', views.compras, name='compras'),
    path('', views.produtos, name='produtos'),
    path('', views.clientes, name='clientes'),
    path('', views.fornecedores, name='fornecedores'),
    path('', views.retirar_produto, name='retirar_produto'),
    path('', views.login, name='login'),
    path('', views.cadastrar_produto, name='cadastrar_produto'),

    ]

