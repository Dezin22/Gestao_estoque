from django.contrib import admin

# Register your models here.

from .models import Produto, Cliente, Compra, Fornecedor, Estoque, Login

admin.site.register(Produto)
admin.site.register(Cliente)
admin.site.register(Compra)
admin.site.register(Fornecedor)
admin.site.register(Estoque)
admin.site.register(Login)

