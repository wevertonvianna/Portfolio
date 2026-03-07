from rest_framework.routers import DefaultRouter
from dezenvolvedor.views.dev import (
    ProjetoViewSet,
    TagViewSet,
    CertificacaoViewSet,
    TecHabilidadeViewSet,
    CarreiraViewSet
)

router = DefaultRouter()

router.register(r"projetos", ProjetoViewSet)
router.register(r"tags", TagViewSet, basename="tags")
router.register(r"certificacoes", CertificacaoViewSet)
router.register(r"habilidades", TecHabilidadeViewSet)
router.register(r"carreira", CarreiraViewSet)

urlpatterns = router.urls