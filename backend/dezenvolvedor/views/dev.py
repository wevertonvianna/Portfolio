from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.filters import OrderingFilter
from dezenvolvedor.models.dev import (
    Projeto,
    Tag,
    Certificacao,
    TecHabilidade,
    Carreira
)
from dezenvolvedor.serializers.dev import (
    ProjetoSerializer,
    TagSerializer,
    CertificacaoSerializer,
    TecHabilidadeSerializer,
    CarreiraSerializer
)


class ProjetoViewSet(ReadOnlyModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer


class TagViewSet(ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CertificacaoViewSet(ReadOnlyModelViewSet):
    queryset = Certificacao.objects.all()
    serializer_class = CertificacaoSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['emitido_em', 'titulo']
    ordering = ['-emitido_em']  # padrão


class TecHabilidadeViewSet(ReadOnlyModelViewSet):
    queryset = TecHabilidade.objects.all()
    serializer_class = TecHabilidadeSerializer


class CarreiraViewSet(ReadOnlyModelViewSet):
    queryset = Carreira.objects.all()
    serializer_class = CarreiraSerializer