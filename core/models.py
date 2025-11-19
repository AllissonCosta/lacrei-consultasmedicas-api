from django.db import models

# 1. Modelo do Profissional
class Profissional(models.Model):
    # Campos de texto (CharField)
    # max_length define o limite de caracteres (segurança e otimização)
    nome_social = models.CharField(max_length=255, help_text="Nome como a pessoa profissional deseja ser chamada")
    profissao = models.CharField(max_length=100, help_text="Ex: Médica, Psicólogo, Enfermeira")
    endereco = models.CharField(max_length=255)
    contato = models.CharField(max_length=100, help_text="Telefone ou e-mail")

    # Isso define como o profissional aparece no painel administrativo do Django
    def __str__(self):
        return f"{self.nome_social} ({self.profissao})"

# 2. Modelo da Consulta
class Consulta(models.Model):
    # Campo de Data e Hora
    data = models.DateTimeField(help_text="Data e hora da consulta")
    
    # RELACIONAMENTO (Chave Estrangeira)
    # Aqui dizemos: "Toda consulta precisa de um profissional vinculado"
    profissional = models.ForeignKey(
        Profissional, 
        on_delete=models.CASCADE, # Se o profissional for deletado, apague as consultas dele também
        related_name='consultas'  # Permite buscar consultas a partir do profissional (ex: doutora.consultas.all())
    )
    
    def __str__(self):
        return f"Consulta com {self.profissional.nome_social} em {self.data}"