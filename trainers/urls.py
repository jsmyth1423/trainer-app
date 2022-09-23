from django.urls import path

from .views import *

urlpatterns = [
    path('list', TrainerList.as_view()),
    path('list-alpha', AlphabeticalTrainerList.as_view()),
    path('list-trained-desc', LastTrainedDescendingTrainerList.as_view()),
    path('list-trained-asc', LastTrainedAscendingTrainerList.as_view()),
    path('<int:pk>/', TrainerDetail.as_view()),
    path('workshop-names', WorkshopNames.as_view()),
    path('workshop-list', WorkshopList.as_view()),
    path('workshop-list-exp-desc', ExpDescendingWorkshopList.as_view()),
    path('workshop-list-exp-asc', ExpAscendingWorkshopList.as_view()),
    path('workshop-list-trained-desc', LastTrainedDescendingWorkshopList.as_view()),
    path('workshop-list-trained-asc', LastTrainedAscendingWorkshopList.as_view()),
    path('clubs', ClubList.as_view()),
]