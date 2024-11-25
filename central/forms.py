from django import forms
from .models import MovimentacaoConta, Conta, Categoria, Pessoa

class MovimentacaoContaForm(forms.ModelForm):
    class Meta:
        model = MovimentacaoConta
        fields = ['titulo', 'valor', 'data', 'conta', 'categoria', 'tipo', 'parcelado', 'parcelas', 'valor_parcelas', 'fixo', 'desconto']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),  # Para o campo de data, define um tipo de input de data
        }

    def __init__(self, *args, **kwargs):
        super(MovimentacaoContaForm, self).__init__(*args, **kwargs)
        # Garantindo que o campo 'desconto' seja definido como False por padrão
        if 'instance' not in kwargs:
            self.fields['desconto'].initial = False
        
        # Garantindo que o campo 'parcelas' tenha um valor inicial de 1
        if 'instance' not in kwargs:
            self.fields['parcelas'].initial = 1
        
        # Garantindo que o campo 'valor_parcelas' tenha valor 0 quando 'parcelado' for False
        if not self.instance.pk or not self.instance.parcelado:
            self.fields['valor_parcelas'].initial = 0
