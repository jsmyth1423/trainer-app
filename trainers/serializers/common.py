from rest_framework import serializers
from ..models import *

class ClubSerializer(serializers.ModelSerializer):

    class Meta:
        model = Club
        fields = ('__all__')

class TrainerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trainer
        fields = ('__all__')
        depth = 1

class WorkshopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Workshop
        fields = ('__all__')

class Workshop_DetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Workshop_Details
        fields = ('id', 'name', 'trainer', 'experience_level',)
        depth = 2


class PopulatedClubSerializer(ClubSerializer):
    trainers = TrainerSerializer(many=True)

    class Meta:
        model = Club
        fields = ('id', 'name', 'location', 'trainers')


class PopulatedTrainerSerializer(TrainerSerializer):
    club = ClubSerializer()




