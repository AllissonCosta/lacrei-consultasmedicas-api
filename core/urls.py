from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfissionalViewSet, ConsultaViewSet

# Cria o "robô" roteador
router = DefaultRouter()

# Cria rotas para Profissionais baseadas na ViewSet
# Obs: O 'r' antes da string indica que é uma "raw string" (padrão em regex/urls)
router.register(r'profissionais', ProfissionalViewSet)

# Cria rotas para Consultas
router.register(r'consultas', ConsultaViewSet)

# Define que as URLs desse arquivo são as que o robô gerou
urlpatterns = [
    path('', include(router.urls)),
]