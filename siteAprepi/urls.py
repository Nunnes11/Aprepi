from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quem-somos/', views.quem_somos, name='quem_somos'),
    path('quem-somos-editar/', views.quem_somos_editar, name='quem_somos_editar'),
    path('historia/', views.historia, name='historia'),
    path('historia-editar/', views.historia_editar, name='historia_editar'),
    path('transparencia/', views.transparencia, name='transparencia'),
    path('documentos-gerais/', views.documentos_gerais, name='documentos_gerais'),
    path('editar-documento-geral/<int:id>/', views.editar_documento_geral, name='editar_documento_geral'),
    path('deletar-documento-geral/<int:id>/', views.deletar_documento_geral, name='deletar_documento_geral'),
    path('atas-reunioes/', views.atas_reunioes, name='atas_reunioes'),
    path('editar-ata-reuniao/<int:id>/', views.editar_ata_reuniao, name='editar_ata_reuniao'),
    path('deletar-ata-reuniao/<int:id>/', views.deletar_ata_reuniao, name='deletar_ata_reuniao'),
    
    path('diretoria/', views.diretoria, name='diretoria'),
    path('diretoria-editar/', views.diretoria_editar, name='diretoria_editar'),
    
    path('registro/', views.registro, name='registro'),
    path('registro_associado/', views.registro_associado, name='registro_associado'),
    path('registro_usuario/', views.registro_usuario, name='registro_usuario'),
    
    path('listar_associados/', views.listar_associados, name='listar_associados'),
    path('detalhar_associado/<int:id>/', views.detalhar_associado, name='detalhar_associado'),
    path('atualizar_associado<int:id>/', views.atualizar_associado, name='atualizar_associado'),
    path('deletar_associado/<int:id>', views.deletar_associado, name='deletar_associado'),
    
    path('listar_usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('detalhar_usuario/<int:id>/', views.detalhar_usuario, name='detalhar_usuario'),
    path('atualizar_usuario/<int:id>/', views.atualizar_usuario, name='atualizar_usuario'),
    path('deletar_usuario/<int:id>/', views.deletar_usuario, name='deletar_usuario'),

    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
