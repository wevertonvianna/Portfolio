from rest_framework import serializers
from dezenvolvedor.models.dev import (Projeto,Tag,Certificacao,TecHabilidade,Carreira)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class ProjetoSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Projeto
        fields = "__all__"


class CertificacaoSerializer(serializers.ModelSerializer):
    emitido_em = serializers.DateField(format="%m/%Y")
    class Meta:
        model = Certificacao
        fields = "__all__"


class TecHabilidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TecHabilidade
        fields = "__all__"


class CarreiraSerializer(serializers.ModelSerializer):
    habilidades = TecHabilidadeSerializer(many=True, read_only=True)

    class Meta:
        model = Carreira
        fields = "__all__"