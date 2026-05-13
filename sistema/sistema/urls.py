from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LogoutView
from sistema.views import Login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('veiculo/', include('veiculo.urls'), name = 'veiculo'),
    path('anuncio/', include('anuncio.urls'), name = 'anuncio'),
]