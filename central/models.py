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
    
    # Campos específicos para cada tipo de movimentação
    origem_ou_motivo = models.CharField(max_length=255, blank=True, null=True)  # Exemplo: "Salário", "Aluguel"
    parcelas = models.PositiveSmallIntegerField(null=True, blank=True)  # Apenas para crédito
    saldo_disponivel = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)  # Apenas para débito
    
    # Campos específicos para PIX
    chave_pix = models.CharField(max_length=255, blank=True, null=True)  # Chave PIX, se for o tipo PIX
    banco_pix = models.CharField(max_length=100, blank=True, null=True)  # Banco associado ao PIX, se for o tipo PIX

    # Novo campo para controlar se a dívida foi paga ou não
    divida_paga = models.BooleanField(default=False)  # False significa que a dívida não foi paga
    
    # Campo para registrar a data em que a dívida foi paga (se aplicável)
    data_pago = models.DateField(null=True, blank=True)  # Caso não tenha sido paga, fica em branco

    def __str__(self):
        return self.titulo
