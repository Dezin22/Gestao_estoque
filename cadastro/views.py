from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Produto, Cliente, Compra, Fornecedor, Estoque, Login

# Create your views here.



def estoque(request):
    estoque_list = Estoque.objects.order_by('-data')
    context = {'estoque_list': estoque_list}
    return render(request, 'cadastro/estoque.html', context)

def compras(request):
    compras_list = Compra.objects.order_by('-data')
    context = {'compras_list': compras_list}
    return render(request, 'cadastro/compras.html', context)

def produtos(request):
    produtos_list = Produto.objects.order_by('-nome')
    context = {'produtos_list': produtos_list}
    return render(request, 'cadastro/produtos.html', context)

def clientes(request):
    clientes_list = Cliente.objects.order_by('-nome')
    context = {'clientes_list': clientes_list}
    return render(request, 'cadastro/clientes.html', context)

def fornecedores(request):
    fornecedores_list = Fornecedor.objects.order_by('-nome')
    context = {'fornecedores_list': fornecedores_list}
    return render(request, 'cadastro/fornecedores.html', context)

def retirar_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    try:
        quantidade = int(request.POST['quantidade'])
    except (KeyError, ValueError):
        return render(request, 'cadastro/produtos.html', {
            'produto': produto,
            'error_message': "Você não digitou um número válido.",
        })
    else:
        if quantidade > produto.quantidade:
            return render(request, 'cadastro/produtos.html', {
                'produto': produto,
                'error_message': "Quantidade indisponível.",
            })
        else:
            produto.quantidade -= quantidade
            produto.save()
            return HttpResponseRedirect(reverse('cadastro:produtos'))
        

def estoque(request):
    estoque_list = Estoque.objects.order_by('-data')
    context = {'estoque_list': estoque_list}
    return render(request, 'cadastro/estoque.html', context)

def index(request):
    return render(request, 'cadastro/index.html')

def login(request):
    login_list = Login.objects.order_by('-login')
    context = {'login_list': login_list}
    return render(request, 'cadastro/login.html', context)

def cadastrar_produto(request):
    nome = request.POST['nome']
    preco = request.POST['preco']
    quantidade = request.POST['quantidade']
    produto = Produto(nome=nome, preco=preco, quantidade=quantidade)
    produto.save()
    return HttpResponseRedirect(reverse('cadastro:produtos'))