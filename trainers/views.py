from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView # Generic classes for CRUD operations

from trainers.serializers.common import PopulatedClubSerializer, PopulatedWorkshopSerializer, TrainerSerializer, PopulatedTrainerSerializer, Workshop_DetailsSerializer, WorkshopSerializer 
import rest_framework_filters as filters

from .models import *
# Create your views here.

#! List of all Trainers
class TrainerList(ListCreateAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    filter_backends = [filters.OrderingFilter]
    search_fields = ['name', 'company_role', 'club__name' ]
    ordering_fields = ['last_trained']

class AlphabeticalTrainerList(ListCreateAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    filter_backends = [filters.OrderingFilter]
    search_fields = ['name', 'company_role', 'club__name' ]
    ordering_fields = ['name']
    ordering = ['name']

#! Pre-determined ordering for last_trained to allow search simultaneously
class LastTrainedDescendingTrainerList(ListCreateAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    filter_backends = [filters.OrderingFilter]
    search_fields = ['name', 'company_role', 'club__name' ]
    ordering_fields = ['last_trained']
    ordering = ['-last_trained']

class LastTrainedAscendingTrainerList(ListCreateAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    filter_backends = [filters.OrderingFilter]
    search_fields = ['name', 'company_role', 'club__name' ]
    ordering_fields = ['last_trained']
    ordering = ['last_trained']


#! Specific View of each Trainer
class TrainerDetail(RetrieveUpdateDestroyAPIView):
    queryset = Trainer.objects.all()
    serializer_class = PopulatedTrainerSerializer

#! List of every experience level from all trainers - different workshops from the same trainer are separate objects
class WorkshopList(ListCreateAPIView):
    queryset = Workshop_Details.objects.all()
    serializer_class = Workshop_DetailsSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['workshop_name', 'experience_level', 'trainer__company_role', 'trainer__name']
    ordering_fields = ['experience_level']


#! Specific views for pre-determined ordering while allowing searches
class ExpDescendingWorkshopList(ListCreateAPIView):
    queryset = Workshop_Details.objects.all()
    serializer_class = Workshop_DetailsSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['workshop_name', 'experience_level', 'trainer__company_role', 'trainer__name']
    ordering_fields = ['experience_level']
    ordering = ['-experience_level']

class ExpAscendingWorkshopList(ListCreateAPIView):
    queryset = Workshop_Details.objects.all()
    serializer_class = Workshop_DetailsSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['workshop_name', 'experience_level', 'trainer__company_role', 'trainer__name']
    ordering_fields = ['experience_level']
    ordering = ['experience_level']

class LastTrainedDescendingWorkshopList(ListCreateAPIView):
    queryset = Workshop_Details.objects.all()
    serializer_class = Workshop_DetailsSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['workshop_name', 'experience_level', 'trainer__company_role', 'trainer__name']
    ordering_fields = ['trainer__last_trained']
    ordering = ['trainer__last_trained']

class LastTrainedAscendingWorkshopList(ListCreateAPIView):
    queryset = Workshop_Details.objects.all()
    serializer_class = Workshop_DetailsSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['workshop_name', 'experience_level', 'trainer__company_role', 'trainer__name']
    ordering_fields = ['trainer__last_trained']
    ordering = ['-trainer__last_trained']



#! List of all Clubs with nested trainers
class ClubList(ListCreateAPIView):
    queryset = Club.objects.all()
    serializer_class = PopulatedClubSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'trainers__last_trained', 'trainers__name']


class WorkshopNames(ListCreateAPIView):
    queryset = Workshop.objects.all()
    serializer_class = PopulatedWorkshopSerializer

