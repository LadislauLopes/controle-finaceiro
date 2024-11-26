# central/views.py
from django.shortcuts import render, redirect
from .forms import MovimentacaoContaForm, CategoriaForm,PessoaForm


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

def adicionar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
          
            form.save()
            return redirect('index')
    else:
        form = CategoriaForm()

    return render(request, 'adicionar_Categoria.html', {'form': form})
def adicionar_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
          
            form.save()
            return redirect('index')
    else:
        form = PessoaForm()

    return render(request, 'adicionar_pessoa.html', {'form': form})
