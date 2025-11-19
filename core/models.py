from django.db import models

# Campo de preenchimento
class Profissional(models.Model):
    # Campo de preenchimento do profissional
    nome_social = models.CharField(max_length=255, help_text="Nome da pessoa")
    profissao = models.CharField(max_length=100, help_text="Ex: Médica, Psicólogo, Enfermeira")
    endereco = models.CharField(max_length=255)
    contato = models.CharField(max_length=100, help_text="Telefone ou e-mail")

    # Isso define como o profissional aparece no painel administrativo do Django
    def __str__(self):
        return f"{self.nome_social} ({self.profissao})"

# Campo de Consulta
class Consulta(models.Model):
    # Campo de Data e Hora
    data = models.DateTimeField(help_text="Data e hora da consulta")
  
    # Aqui faz com que toda consulta vai ter um profissional vinculado"
    profissional = models.ForeignKey(
        Profissional, 
        on_delete=models.CASCADE, # Se o profissional for deletado, apaga as consultas dele também
        related_name='consultas'  # Permite buscar consultas a partir do profissional
    )
    
    def __str__(self):
        return f"Consulta com {self.profissional.nome_social} em {self.data}"