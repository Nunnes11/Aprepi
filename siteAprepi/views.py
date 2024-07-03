from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import QuemSomosForm, HistoriaForm, DocumentoGeralForm, AtaReuniaoForm, DiretoriaForm, AssociadoForm, UsuarioForm
from .models import QuemSomos, Historia, DocumentoGeral, AtaReuniao, Diretoria, Associado, Usuario


def home(request):
    return render(request, 'siteAprepi/home.html')


# views para link APREPI

def quem_somos(request):
    quem_somos_conteudo = QuemSomos.objects.first()
    return render(request, 'siteAprepi/quem_somos.html', {'quem_somos_conteudo': quem_somos_conteudo})


def is_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(is_admin)
def quem_somos_editar(request):
    quem_somos_conteudo = get_object_or_404(QuemSomos, pk=1)
    if request.method == 'POST':
        form = QuemSomosForm(request.POST, request.FILES, instance=quem_somos_conteudo)
        if form.is_valid():
            form.save()
            return redirect('quem_somos')
    else:
        form = QuemSomosForm(instance=quem_somos_conteudo)
    return render(request, 'siteAprepi/quem_somos_editar.html', {'form':form})


def historia(request):
    conteudo = Historia.objects.first()
    return render(request, 'siteAprepi/historia.html', {'conteudo':conteudo})

def is_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(is_admin)
def historia_editar(request):
    conteudo = get_object_or_404(Historia, pk=1)
    if request.method == 'POST':
        form = HistoriaForm(request.POST, request.FILES, instance=conteudo)
        if form.is_valid():
            form.save()
            return redirect('historia')
    else:
        form = HistoriaForm(instance=conteudo)
    return render(request, 'siteAprepi/historia_editar.html', {'form':form})


def transparencia(request):
    documentos_gerais = DocumentoGeral.objects.all()
    atas_reunioes = AtaReuniao.objects.all()
    return render(request, 'siteAprepi/transparencia.html', {
        'documentos_gerais':documentos_gerais,
        'atas_reunioes':atas_reunioes,
    })


def is_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(is_admin)
def documentos_gerais(request):
    if request.method == 'POST':
        form = DocumentoGeralForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('transparencia')
    else:
        form = DocumentoGeralForm()
    return render(request, 'siteAprepi/documentos_gerais.html', {'form':form})

@login_required
@user_passes_test(is_admin)
def editar_documento_geral(request, id):
    documento = get_object_or_404(DocumentoGeral, id=id)
    if request.method == 'POST':
        form = DocumentoGeralForm(request.POST, request.FILES, instance=documento)
        if form.is_valid():
            form.save()
            return redirect('transparencia')
    else:
        form = DocumentoGeralForm(instance=documento)
    return render(request, 'siteAprepi/editar_documento_geral.html', {'form':form})


@login_required
@user_passes_test(is_admin)
def deletar_documento_geral(request, id):
    documento = get_object_or_404(DocumentoGeral, id=id)
    if request.method == 'POST':
        documento.delete()
        return redirect('transparencia')
    return render(request, 'siteAprepi/deletar_documento_geral.html', {'documento':documento})


@login_required
@user_passes_test(is_admin)
def atas_reunioes(request):
    if request.method == 'POST':
        form = AtaReuniaoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('transparencia')
    else:
        form = AtaReuniaoForm()
    return render(request, 'siteAprepi/atas_reunioes.html', {'form':form})

@login_required
@user_passes_test(is_admin)
def editar_ata_reuniao(request, id):
    ata = get_object_or_404(AtaReuniao, id=id)
    if request.method == 'POST':
        form = AtaReuniaoForm(request.POST, request.FILES, instance=ata)
        if form.is_valid:
            form.save()
            return redirect('transparencia')
    else:
        form = AtaReuniaoForm(instance=ata)
    return render(request, 'siteAprepi/editar_ata_reuniao.html', {'form':form})

@login_required
@user_passes_test(is_admin)
def deletar_ata_reuniao(request, id):
    ata = get_object_or_404(AtaReuniao, id=id)
    if request.method == 'POST':
        ata.delete()
        return redirect('transparencia')
    return render(request, 'siteAprepi/deletar_ata_reuniao.html', {'ata':ata})


# Views para link DIRETORIA

def diretoria(request):
    conteudo = Diretoria.objects.first()
    return render(request, 'siteAprepi/diretoria.html', {'conteudo':conteudo})

@login_required
@user_passes_test(is_admin)
def diretoria_editar(request):
    conteudo = get_object_or_404(Diretoria, pk=1)
    if request.method == 'POST':
        form = DiretoriaForm(request.POST, request.FILES, instance=conteudo)
        if form.is_valid:
            form.save()
            return redirect('diretoria')
    else:
        form = DiretoriaForm(instance=conteudo)
    return render(request, 'siteAprepi/diretoria_editar.html', {'form':form})

# Views para REGISTRO

def registro(request):
    return render(request, 'siteAprepi/registro.html')

def registro_associado(request):
    if request.method == 'POST':
        form = AssociadoForm(request.POST)
        if form.is_valid():
            associado = form.save()
            user = associado.user
            user.set_password(form.cleaned_data['password'])
            user.save()
            user = authenticate(username=user.username, password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
            return redirect('listar_associados')
    else:
        form = AssociadoForm()
    return render(request, 'siteAprepi/registro_associado.html', {'form':form})


def registro_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'siteAprepi/registro_usuario.html', {'form':form})


# Views para listar, detalhar, atualizar e deletar Associados:

@login_required
@user_passes_test(lambda u: u.is_superuser)
def listar_associados(request):
    associados = Associado.objects.all()
    return render(request, 'siteAprepi/listar_associados.html', {'associados':associados})

def detalhar_associado(request, id):
    associado = get_object_or_404(Associado, id=id)
    return render(request, 'siteAprepi/detalhar_associado.html', {'associado':associado})

def atualizar_associado(request, id):
    associado = get_object_or_404(Associado, id=id)
    if request.method == 'POST':
        form = AssociadoForm(request.POST, instance=associado)
        if form.is_valid():
            form.save()
            return redirect('listar_associados')
    else:
        form = AssociadoForm(instance=associado)
    return render(request, 'siteAprepi/atualizar_associado.html', {'form':form})


def deletar_associado(request, id):
    associado = get_object_or_404(Associado, id=id)
    if request.method == 'POST':
        associado.delete()
        return redirect('listar_associados')
    return render(request, 'siteAprepi/deletar_associado.html', {'associado':associado})


# Views para listar, detalhar, atualizar e deletar Usuário:

@login_required
@user_passes_test(lambda u: u.is_superuser)
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'siteAprepi/listar_usuarios.html', {'usuarios': usuarios})


def detalhar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    return render(request, 'siteAprepi/detalhar_usuario.html', {'usuario':usuario})


def atualizar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'siteAprepi/atualizar_usuario.html', {'form':form})


def deletar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listar_usuarios')
    return render(request, 'siteAprepi/deletar_usuario.html', {'usuario':usuario})


# Criando as funcionalidades para LOGIN:

class LoginView(LoginView):
    template_name = 'siteAprepi/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')




