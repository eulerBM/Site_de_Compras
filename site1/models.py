from django.db import models

class produto(models.Model):
    nome = models.CharField(max_length=20)
    descricao = models.TextField(max_length=100)

    class Meta:
        db_table = 'produtos'

