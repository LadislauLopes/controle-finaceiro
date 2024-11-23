from django.db import models

class Pessoa(models.Model):
    id_pessoa = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Conta(models.Model):
    id_Conta = models.AutoField(primary_key=True)
    Banco = models.CharField(max_length=255)
    id_pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return f"Conta de {self.id_pessoa.nome}"

class MovimentacaoConta(models.Model):
    TIPO_CHOICES = [
        ('CREDITO', 'Crédito'),
        ('DEBITO', 'Débito'),
        ('DEPOSITO_FIXO', 'Depósito Fixo'),
        ('DESCONTO_FIXO', 'Desconto Fixo'),
        ('PIX', 'PIX'),
    ]

    titulo = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    conta = models.ForeignKey('Conta', on_delete=models.CASCADE)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    parcelas = models.SmallIntegerField(null=True, blank=True, default=0)  
    valor_parcelas =  models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)  
    fixo= models.BooleanField(default=False)
    desconto = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
