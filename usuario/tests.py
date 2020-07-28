from django.test import TestCase, Client
from django.contrib import messages

from .models import Usuario

class UsuarioTestCase(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create(nome='Rafael')

    def test_str_retorna_nome(self):
        self.assertEqual(str(self.usuario), 'Rafael')

    def test_cadastrar_usuario_ja_existente(self):
        client = Client()
        response = client.post(
            '/usuarios/create',
            {
                'nome': 'Rafael'
            }
        )

        storage = messages.get_messages(response.wsgi_request)
        for msg in storage:
            self.assertEqual(str(msg), 'O usuário Rafael já está cadastrado')

    def test_editar_usuario_ja_existente(self):
        client = Client()
        response = client.post(
            '/usuarios/update/1',
            {
                'nome': 'Rafael'
            }
        )

        storage = messages.get_messages(response.wsgi_request)
        for msg in storage:
            self.assertEqual(str(msg), 'O usuário Rafael já está cadastrado')