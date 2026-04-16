from django.urls import path
from veiculo.views import *

urlpatterns = [
    path('listar-veiculo/', ListarVeiculos.as_view(), name='listar-veiculos'),
    path('novo/', CriarVeiculos.as_view(), name='criar-veiculos'),

    path('editar/<int:pk>/' , EditarVeiculos.as_view(), name = 'editar-veiculo'),
    path('fotos/<str:arquivo>/', FotoVeiculo.as_view(), name='foto-veiculo'),
]