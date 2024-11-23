# central/views.py
from django.shortcuts import render, redirect
from .forms import MovimentacaoContaForm


def index(request):
    return render(request, 'index.html')

def adicionar_entrada(request):
    if request.method == 'POST':
        form = MovimentacaoContaForm(request.POST)
        if form.is_valid():
            # Aqui, o desconto já é False por padrão, pois configuramos no formulário
            form.save()
            return redirect('index')  # Você pode redirecionar para a página principal ou qualquer outra página
    else:
        form = MovimentacaoContaForm()

    return render(request, 'adicionar_entrada.html', {'form': form})
