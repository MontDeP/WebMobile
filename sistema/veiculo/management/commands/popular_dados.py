import decimal
import urllib.request

from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from anuncio.models import Anuncio
from veiculo.models import Veiculo

VEICULOS = [
    {
        'marca': 1, 'modelo': 'Corolla Cross', 'ano': 2023, 'cor': 2, 'combustivel': 4,
        'img': 'https://loremflickr.com/800/500/toyota,corolla?lock=101',
    },
    {
        'marca': 2, 'modelo': 'Civic Touring', 'ano': 2022, 'cor': 1, 'combustivel': 1,
        'img': 'https://loremflickr.com/800/500/honda,civic?lock=102',
    },
    {
        'marca': 3, 'modelo': 'Mustang GT', 'ano': 2021, 'cor': 5, 'combustivel': 1,
        'img': 'https://loremflickr.com/800/500/ford,mustang?lock=103',
    },
    {
        'marca': 4, 'modelo': 'Onix Plus', 'ano': 2023, 'cor': 3, 'combustivel': 4,
        'img': 'https://loremflickr.com/800/500/chevrolet,car?lock=104',
    },
    {
        'marca': 5, 'modelo': 'Golf GTI', 'ano': 2022, 'cor': 4, 'combustivel': 1,
        'img': 'https://loremflickr.com/800/500/volkswagen,golf?lock=105',
    },
    {
        'marca': 6, 'modelo': 'Sentra SV', 'ano': 2023, 'cor': 6, 'combustivel': 1,
        'img': 'https://loremflickr.com/800/500/nissan,car?lock=106',
    },
    {
        'marca': 7, 'modelo': 'HB20 Diamond', 'ano': 2022, 'cor': 2, 'combustivel': 4,
        'img': 'https://loremflickr.com/800/500/hyundai,car?lock=107',
    },
    {
        'marca': 8, 'modelo': 'Stinger GT', 'ano': 2021, 'cor': 1, 'combustivel': 1,
        'img': 'https://loremflickr.com/800/500/kia,car?lock=108',
    },
    {
        'marca': 9, 'modelo': 'Kwid Intense', 'ano': 2023, 'cor': 7, 'combustivel': 4,
        'img': 'https://loremflickr.com/800/500/renault,car?lock=109',
    },
    {
        'marca': 10, 'modelo': '208 Griffe', 'ano': 2022, 'cor': 4, 'combustivel': 1,
        'img': 'https://loremflickr.com/800/500/peugeot,car?lock=110',
    },
]

ANUNCIOS = [
    {
        'veiculo_idx': 0,
        'titulo': 'Toyota Corolla Cross impecável',
        'descricao': 'Único dono, revisões em dia na concessionária. IPVA 2024 pago. Aceita financiamento.',
        'valor': '95000.00',
    },
    {
        'veiculo_idx': 1,
        'titulo': 'Honda Civic Touring com teto solar',
        'descricao': 'Completo, multimídia original, câmera de ré e sensores de estacionamento. Aceita troca.',
        'valor': '115000.00',
    },
    {
        'veiculo_idx': 2,
        'titulo': 'Ford Mustang GT V8 — raridade',
        'descricao': 'Motor 5.0 V8, 450cv, câmbio automático. Poucas unidades no Brasil. Oportunidade única.',
        'valor': '320000.00',
    },
    {
        'veiculo_idx': 3,
        'titulo': 'Onix Plus Premier — aceita financiamento',
        'descricao': 'Central multimídia, ar-condicionado, direção elétrica. Econômico e completo. Parcelo em até 60x.',
        'valor': '89000.00',
    },
    {
        'veiculo_idx': 4,
        'titulo': 'VW Golf GTI — esportivo europeu',
        'descricao': 'Motor 2.0 TSI turbo, 230cv. Suspensão esportiva, bancos em couro, controles no volante.',
        'valor': '180000.00',
    },
    {
        'veiculo_idx': 5,
        'titulo': 'Nissan Sentra SV completo',
        'descricao': 'CVT, câmera 360°, piloto automático adaptativo. Baixo km rodado. Ideal para família.',
        'valor': '105000.00',
    },
    {
        'veiculo_idx': 6,
        'titulo': 'HB20 Diamond — pronto para rodar',
        'descricao': 'Revisões em dia, pneus novos, ar-condicionado gelando. Ideal para cidade. Aceita troca menor.',
        'valor': '75000.00',
    },
    {
        'veiculo_idx': 7,
        'titulo': 'Kia Stinger GT — esportivo coreano',
        'descricao': 'V6 biturbo 370cv, tração traseira. Design exclusivo, som Harman Kardon. Raridade no Brasil.',
        'valor': '270000.00',
    },
]


def baixar_imagem(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=20) as resp:
            return resp.read()
    except Exception as e:
        return None


class Command(BaseCommand):
    help = 'Popula o banco com veículos e anúncios de exemplo'

    def handle(self, *args, **options):
        user, created = User.objects.get_or_create(
            username='admin',
            defaults={'is_staff': True, 'is_superuser': True},
        )
        if created:
            user.set_password('admin123')
            user.save()
            self.stdout.write(self.style.SUCCESS('Usuário admin criado — senha: admin123'))
        else:
            self.stdout.write(f'Usando usuário existente: {user.username}')

        veiculos_criados = []

        for v in VEICULOS:
            self.stdout.write(f"Criando {v['modelo']}...", ending=' ')
            veiculo = Veiculo.objects.create(
                marca=v['marca'],
                modelo=v['modelo'],
                ano=v['ano'],
                cor=v['cor'],
                combustivel=v['combustivel'],
            )

            img_data = baixar_imagem(v['img'])
            if img_data:
                nome = f"{v['modelo'].lower().replace(' ', '_')}.jpg"
                veiculo.foto.save(nome, ContentFile(img_data), save=True)
                self.stdout.write(self.style.SUCCESS('imagem OK'))
            else:
                self.stdout.write(self.style.WARNING('sem imagem'))

            veiculos_criados.append(veiculo)

        self.stdout.write('')
        for a in ANUNCIOS:
            veiculo = veiculos_criados[a['veiculo_idx']]
            Anuncio.objects.create(
                titulo=a['titulo'],
                descricao=a['descricao'],
                valor=decimal.Decimal(a['valor']),
                veiculo=veiculo,
                usuario=user,
            )
            self.stdout.write(f"  Anúncio: {a['titulo']}")

        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS(
            f'Concluído: {len(veiculos_criados)} veículos e {len(ANUNCIOS)} anúncios criados.'
        ))
