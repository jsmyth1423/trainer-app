from urllib import response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView # Generic classes for CRUD operations

from trainers.serializers.common import PopulatedClubSerializer, TrainerSerializer, PopulatedTrainerSerializer, Workshop_DetailsSerializer 
from rest_framework import filters



from .models import *
# Create your views here.


class TrainerList(ListCreateAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

class TrainerDetail(RetrieveUpdateDestroyAPIView):
    queryset = Trainer.objects.all()
    serializer_class = PopulatedTrainerSerializer

class WorkshopList(ListCreateAPIView):
    queryset = Workshop_Details.objects.all()
    serializer_class = Workshop_DetailsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'experience_level', 'trainer__company_role']

class ClubList(ListCreateAPIView):
    queryset = Club.objects.all()
    serializer_class = PopulatedClubSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    # search by andi level
