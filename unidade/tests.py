from django.test import TestCase, Client
from django.contrib import messages

from .models import Unidade

class UnidadeTestCase(TestCase):
    def setUp(self):
        self.unidade = Unidade.objects.create(sigla='kg', digitos=2)

    def test_str_retorna_sigla(self):
        self.assertEqual(str(self.unidade), 'kg')

    def test_cadastrar_unidade_ja_existente(self):
        client = Client()
        response = client.post(
            '/unidades/create',
            {
                'sigla': 'kg',
                'digitos': 2
            }
        )

        storage = messages.get_messages(response.wsgi_request)
        for msg in storage:
            self.assertEqual(str(msg), 'A unidade kg já está cadastrada')

    def test_editar_unidade_ja_existente(self):
        self.unidade = Unidade.objects.create(sigla='cm', digitos=2)
        client = Client()
        response = client.post(
            '/unidades/update/2',
            {
                'sigla': 'kg',
                'digitos': 2
            }
        )

        storage = messages.get_messages(response.wsgi_request)
        for msg in storage:
            self.assertEqual(str(msg), 'A unidade kg já está cadastrada')

    def test_cadastrar_unidade_com_digito_negativo(self):
        client = Client()
        response = client.post(
            '/unidades/create',
            {
                'sigla': 'cm',
                'digitos': -1
            }
        )

        storage = messages.get_messages(response.wsgi_request)
        for msg in storage:
            self.assertEqual(str(msg), 'A quantidade de dígitos não pode ser negativa')

    def test_editar_unidade_com_digito_negativo(self):
        client = Client()
        response = client.post(
            '/unidades/update/1',
            {
                'sigla': 'kg',
                'digitos': -1
            }
        )

        storage = messages.get_messages(response.wsgi_request)
        for msg in storage:
            self.assertEqual(str(msg), 'A quantidade de dígitos não pode ser negativa')
