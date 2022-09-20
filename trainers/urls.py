from django.urls import path

from .views import ClubList, TrainerList, TrainerDetail, WorkshopList

urlpatterns = [
    path('', TrainerList.as_view()),
    path('<int:pk>/', TrainerDetail.as_view()),
    path('details', WorkshopList.as_view()),
    path('clubs', ClubList.as_view()),
]