from django.test import TestCase, Client
from django.contrib import messages
from datetime import datetime, timedelta

from .models import Acompanhamento
from usuario.models import Usuario
from metrica.models import Metrica
from unidade.models import Unidade

class AcompanhamentoTestCase(TestCase):
    def setUp(self):
        usuario = Usuario.objects.create(nome='Rafael')
        unidade = Unidade.objects.create(sigla='kg', digitos=2)
        metrica = Metrica.objects.create(nome='Peso', unidade=unidade)
        self.acompanhamento = Acompanhamento.objects.create(
            dt_medicao=datetime.strptime('2020-01-01', '%Y-%m-%d').date(),
            medida=90,
            metrica=metrica,
            usuario=usuario
        )

    def test_str_retorna_data_medicao_e_metrica(self):
        self.assertEqual(str(self.acompanhamento), '2020-01-01 - Peso')

    def test_cadastrar_acompanhamento_com_data_futura(self):
        client = Client()
        response = client.post(
            '/acompanhamentos/create',
            {
                'dt_medicao': datetime.now().date() + timedelta(days=1),
                'medida': 90,
                'metrica': 1,
                'usuario': 1
            }
        )

        storage = messages.get_messages(response.wsgi_request)
        for msg in storage:
            self.assertEqual(str(msg), 'A data de medição não pode ser posterior ao dia de hoje')

    def test_editar_acompanhamento_com_data_futura(self):
        client = Client()
        response = client.post(
            '/acompanhamentos/update/1',
            {
                'dt_medicao': datetime.now().date() + timedelta(days=1),
                'medida': 90,
                'metrica': 1,
                'usuario': 1
            }
        )

        storage = messages.get_messages(response.wsgi_request)
        for msg in storage:
            self.assertEqual(str(msg), 'A data de medição não pode ser posterior ao dia de hoje')

    def test_cadastrar_acompanhamento_com_medida_negativa(self):
        client = Client()
        response = client.post(
            '/acompanhamentos/create',
            {
                'dt_medicao': datetime.now().date(),
                'medida': -1,
                'metrica': 1,
                'usuario': 1
            }
        )

        storage = messages.get_messages(response.wsgi_request)
        for msg in storage:
            self.assertEqual(str(msg), 'O valor da medida não pode ser negativo')

    def test_editar_acompanhamento_com_medida_negativa(self):
        client = Client()
        response = client.post(
            '/acompanhamentos/update/1',
            {
                'dt_medicao': datetime.now().date(),
                'medida': -1,
                'metrica': 1,
                'usuario': 1
            }
        )

        storage = messages.get_messages(response.wsgi_request)
        for msg in storage:
            self.assertEqual(str(msg), 'O valor da medida não pode ser negativo')
