from django.db import models

# Create your models here.


    
class Produto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.FloatField()
    quantidade = models.IntegerField()
    
    

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    
class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    valor_unitario = models.FloatField()
    quantidade = models.IntegerField()
    data = models.DateTimeField('data da venda')
    

class Fornecedor(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    

class Estoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    data = models.DateTimeField('data da entrada')
    
class Login(models.Model):
    login = models.CharField(max_length=200)
    senha = models.CharField(max_length=200)

class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    login = models.ForeignKey(Login, on_delete=models.CASCADE)
    

 