from django.views.generic import View
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate as authrenticate, login

class Login(View):

    """
    class based view para autenticacao de usuarios
    """

    def get(self, request):
        context = {}
        return render(request, 'autenticacao.html', context)
    
    def post(self, request):
        usuario = request.POST.get('usuario', None)
        senha = request.POST.get('senha', None)

        user = authrenticate(request, username=usuario, password=senha)
        if user is not None:
            #verificar se esta ativo
            if user.is_active:
                login(request, user)
                return redirect("listar-veiculos")
            else:
                return render(request, 'autenticacao.html', {"mensagem": "Usuario inativo"})
        return render (request, 'autenticacao.html', {"mensagem": "Usuario ou senha invalidos"})