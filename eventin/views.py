from rest_framework import viewsets, generics, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Evento, Participante, Inscricao
from .serializers import (
    EventoSerializer, ParticipanteSerializer, InscricaoSerializer, 
    ListaInscricoesEventoSerializer, ListaInscricoesParticipantesSerializer,
    ParticipanteSerializerV2
)
from django_filters.rest_framework import DjangoFilterBackend

class EventoViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class ParticipanteViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Participante.objects.all()
    #serializer_class = ParticipanteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']
    def get_serializer_class(self):
        if self.request.version == "v2":
            return ParticipanteSerializerV2
        return ParticipanteSerializer

class InscricaoViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Inscricao.objects.all()
    serializer_class = InscricaoSerializer

class ListaInscricoesParticipante(generics.ListAPIView):
    serializer_class = ListaInscricoesParticipantesSerializer

    def get_queryset(self):
        participante_id = self.kwargs["pk"]
        return Inscricao.objects.filter(participante_id=participante_id)
    
class ListaInscricoesEvento(generics.ListAPIView):
    serializer_class = ListaInscricoesEventoSerializer

    def get_queryset(self):
        evento_id = self.kwargs["pk"]
        return Inscricao.objects.filter(evento_id=evento_id)