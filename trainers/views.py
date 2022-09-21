from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView # Generic classes for CRUD operations

from trainers.serializers.common import PopulatedClubSerializer, TrainerSerializer, PopulatedTrainerSerializer, Workshop_DetailsSerializer 
from rest_framework import filters




from .models import *
# Create your views here.

#! List of all Trainers
class TrainerList(ListCreateAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['ANDi_level']

#! Specific View of each Trainer - doesn't currently show which workshops they have experience_levels in (needs to)
class TrainerDetail(RetrieveUpdateDestroyAPIView):
    queryset = Trainer.objects.all()
    serializer_class = PopulatedTrainerSerializer

#! List of every experience level from all trainers - different workshops from the same trainer are separate objects
class WorkshopList(ListCreateAPIView):
    queryset = Workshop_Details.objects.all()
    serializer_class = Workshop_DetailsSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['workshop_name', 'experience_level', 'trainer__company_role', '=trainer__name']
    ordering_fields = ['experience_level', 'trainer__ANDi_level']



#! List of all Clubs with nested trainers
class ClubList(ListCreateAPIView):
    queryset = Club.objects.all()
    serializer_class = PopulatedClubSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'trainers__last_trained']
    ordering_fields = ['trainers__last_trained']
