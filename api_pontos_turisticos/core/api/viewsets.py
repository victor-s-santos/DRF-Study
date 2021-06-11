from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.decorators import action


class PontoTuristicoViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    #queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)
    """
    #subrescrevendo list
    def list(self, request, *args, **kwargs):
        return Response('list')
    """
    """
    #subrescrevendo create
    def create(self, request, *args, **kwargs):
        pass
    """
    """
    #subrescrevendo delete
    def destroy(self, request, *args, **kwargs):
        pass
    """

    """
    #subscrevendo retrieve
    def retrieve(self, request, *args, **kwargs):
        pass
    """

    """
    #subscrevendo o update
    def update(self, request, *args, **kwargs):
        pass
    """
    """
    #subscrevendo o partial update
    def partial_update(self, request, *args, **kwargs):
        pass
    """

    #funcao customizada
    """@action(methods=['GET'], detail=True)
    def denunciar(self, request, pk=None):
        pass"""