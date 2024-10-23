from django.db import models
import datetime
from django.utils import timezone
# Create your models here.


    
class Produto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.FloatField()
    quantidade = models.IntegerField()
    
    def __str__(self):
        return self.nome
    

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nome
class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    valor_unitario = models.FloatField()
    quantidade = models.IntegerField()
    data = models.DateTimeField('data da venda')
    
    def __str__(self):
        return self.cliente.nome + ' - ' + self.produto.nome + ' - ' + str(self.data)

class Fornecedor(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nome

class Estoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    data = models.DateTimeField('data da entrada')

    def __str__(self):
        return f'{self.produto.nome} - {self.fornecedor.nome} - {self.data}'
    
class Login(models.Model):
    login = models.CharField(max_length=200)
    senha = models.CharField(max_length=200)
    
    def __str__(self):
        return self.login
    
class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    login = models.ForeignKey(Login, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome

 