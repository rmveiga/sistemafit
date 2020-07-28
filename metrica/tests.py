from django.test import TestCase, Client
from django.contrib import messages

from .models import Metrica
from unidade.models import Unidade

class MetricaTestCase(TestCase):
    def setUp(self):
        self.unidade = Unidade.objects.create(sigla='kg', digitos=2)
        self.metrica = Metrica.objects.create(nome='Peso', unidade=self.unidade)

    def test_str_retorna_nome(self):
        self.assertEqual(str(self.metrica), 'Peso')

    def test_cadastrar_metrica_ja_existente(self):
        client = Client()
        response = client.post(
            '/metricas/create',
            {
                'nome': 'Peso',
                'unidade': 1
            }
        )

        storage = messages.get_messages(response.wsgi_request)
        for msg in storage:
            self.assertEqual(str(msg), 'A métrica Peso já está cadastrada')

    def test_editar_metrica_ja_existente(self):
        self.metrica = Metrica.objects.create(nome='Cintura', unidade=self.unidade)
        client = Client()
        response = client.post(
            '/metricas/update/2',
            {
                'nome': 'Peso',
                'unidade': 1
            }
        )

        storage = messages.get_messages(response.wsgi_request)
        for msg in storage:
            self.assertEqual(str(msg), 'A métrica Peso já está cadastrada')
