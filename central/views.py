# central/views.py
from django.shortcuts import render, redirect
from .forms import MovimentacaoContaForm, CategoriaForm,PessoaForm,ContaForm
from django.db.models import Sum
from .models import MovimentacaoConta


def index(request):
    total_valor = MovimentacaoConta.objects.filter(desconto=False).aggregate(total=Sum('valor'))['total']
    
    context = {
        'total_valor': total_valor
    }
    
    return render(request, 'index.html', context)


def adicionar_mov(request):
    if request.method == 'POST':
        form = MovimentacaoContaForm(request.POST)
        if form.is_valid():
            # Aqui, o desconto já é False por padrão, pois configuramos no formulário
            form.save()
            return redirect('index')  # Você pode redirecionar para a página principal ou qualquer outra página
    else:
        form = MovimentacaoContaForm()

    return render(request, 'adicionar_mov.html', {'form': form})

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



def adicionar_conta(request):
    if request.method == "POST":
        form = ContaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redireciona após salvar
    else:
        form = ContaForm()

    return render(request, 'adicionar_conta.html', {'form': form})