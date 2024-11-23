from django import forms
from .models import MovimentacaoConta, Conta, Categoria

class MovimentacaoContaForm(forms.ModelForm):
    class Meta:
        model = MovimentacaoConta
        fields = ['titulo', 'valor', 'data', 'conta', 'categoria', 'tipo', 'parcelas', 'valor_parcelas', 'fixo', 'desconto']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),  # Para o campo de data, define um tipo de input de data
        }

    def __init__(self, *args, **kwargs):
        super(MovimentacaoContaForm, self).__init__(*args, **kwargs)
        # Aqui, garantimos que o campo 'desconto' é definido como False por padrão.
        if 'instance' not in kwargs:
            self.fields['desconto'].initial = False
