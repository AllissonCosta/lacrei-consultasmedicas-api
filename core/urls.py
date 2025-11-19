from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfissionalViewSet, ConsultaViewSet

# 1. Criamos o "robô" roteador
router = DefaultRouter()

# 2. Dizemos ao robô: "Crie rotas para Profissionais baseadas nessa ViewSet"
# O 'r' antes da string indica que é uma "raw string" (padrão em regex/urls)
router.register(r'profissionais', ProfissionalViewSet)

# 3. Dizemos ao robô: "Crie rotas para Consultas também"
router.register(r'consultas', ConsultaViewSet)

# 4. Definimos que as URLs desse arquivo são as que o robô gerou
urlpatterns = [
    path('', include(router.urls)),
]