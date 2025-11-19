from rest_framework.test import APITestCase
from rest_framework import status
from .models import Profissional, Consulta
from django.contrib.auth.models import User # <--- Importamos o modelo de Usuário

class ProfissionalTests(APITestCase):
    
    def setUp(self):
        # 1. CRIAR UM USUÁRIO DE TESTE
        # Precisamos de alguém para "ser" o dono da requisição
        self.user = User.objects.create_user(username='testuser', password='password123')

        # 2. FORÇAR AUTENTICAÇÃO
        # Aqui dizemos: "Client, aja como se o 'self.user' estivesse logado"
        self.client.force_authenticate(user=self.user)

        self.url_list = '/api/profissionais/'
        
        self.dados_profissional = {
            "nome_social": "Dra. Ana Silva",
            "profissao": "Cardiologista",
            "endereco": "Rua das Flores, 123",
            "contato": "ana@email.com"
        }

    def test_create_profissional(self):
        """Teste 1: Tenta criar um profissional via API (Autenticado)"""
        response = self.client.post(self.url_list, self.dados_profissional, format='json')
        
        if response.status_code != 201:
            print("\nERRO NO CREATE:", response.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profissional.objects.count(), 1)

    def test_list_profissionais(self):
        """Teste 2: Tenta listar profissionais (Autenticado)"""
        Profissional.objects.create(**self.dados_profissional)
        
        response = self.client.get(self.url_list)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_profissional_missing_data(self):
        """Teste 3: Tenta criar faltando dados"""
        dados_incompletos = {"nome_social": "Dra. Incompleta"}
        
        response = self.client.post(self.url_list, dados_incompletos, format='json')
        
        # Agora vai dar 400 (Bad Request) e não 401 (Unauthorized),
        # porque o usuário está logado, mas mandou dados ruins.
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_unauthorized_access(self):
        """Teste 4 (NOVO): Garante que quem NÃO tem login toma erro 401"""
        # Deslogamos o usuário forçadamente para este teste específico
        self.client.force_authenticate(user=None)
        
        response = self.client.get(self.url_list)
        
        # Agora esperamos o 401!
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)