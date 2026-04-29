from django.urls import path
from veiculo.views import *

urlpatterns = [
    path('listar-veiculo/', ListarVeiculos.as_view(), name='listar-veiculos'),
    path('fotos/<path:arquivo>',FotoVeiculo.as_view(), name='foto-veiculo'),
    path('editar/<int:pk>/',EditarVeiculo.as_view(), name='editar-veiculo'),
    path('novo/',CriarVeiculo.as_view(), name='criar-veiculo'),
    path('excluir/<int:pk>/',ExcluirVeiculo.as_view(), name='excluir-veiculo')
]