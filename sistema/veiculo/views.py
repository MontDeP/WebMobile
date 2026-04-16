from django.http import FileResponse, Http404
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from veiculo.models import Veiculo
from django.views.generic import CreateView
from .forms import FormularioVeiculo
from django.urls import reverse_lazy

class ListarVeiculos(LoginRequiredMixin, ListView):
    """
    View para listar os veículos cadastrados.
    """
    model = Veiculo
    context_object_name = 'veiculos'
    template_name = 'veiculo/listar.html'

    def get_queryset(self, **kwargs):
        pesquisa = self.request.GET.get('pesquisa' , None)
        queryset = Veiculo.objects.all()
        if pesquisa is not None:
            queryset = queryset.filter(modelo__icontains=pesquisa)
        return queryset
    
class CriarVeiculos(LoginRequiredMixin, CreateView):
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/novo.html'
    success_url = reverse_lazy('listar-veiculos')
    
class EditarVeiculos(CreateView):
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/editar.html'
    success_url = reverse_lazy('listar-veiculos')

class FotoVeiculo(ListView):

    def get(self, request, arquivo):
        try:
            veiculo = Veiculo.objects.get(foto='veiculo/fotos/{}.format(arquivo)')
            return FileResponse(veiculo.foto)
        except Veiculo.DoesNotExist:
            raise Http404("Foto não encontrada ou acesso não autorizado")
        except Exception as exception:
            raise exception
