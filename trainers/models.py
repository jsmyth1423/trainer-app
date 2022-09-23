from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

#! Choice Arrays for dropdown selectors
company_role_choices = [
    ("Product Developer", "Product Developer"),
    ("Product Analyst", "Product Analyst"),
    ("Squad Lead", "Squad Lead"),
    ("Cloud Engineer", "Cloud Engineer"),
    ("Onboarding Coordinator", "Onboarding Coordinator"),
    ("Principal Consultant", "Principal Consultant")
]

experience_level = [
    ("0 - No experience", "0 - No experience"),
    ("1 - Shadowing", "1 - Shadowing"),
    ("2 - Co-run a workshop", "2 - Co-run a workshop"),
    ("3 - Lead a workshop with support", "3 - Lead a workshop with support"),
    ("4 - Lead workshop independently", "4 - Lead workshop independently"),
    ("5 - Trains others to run workshops", "5 - Trains others to run workshops")
]

# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

class Trainer(models.Model):
    name = models.CharField(max_length=50)
    club = models.ForeignKey(
        Club, related_name='trainers', blank=True, on_delete=models.SET_NULL, null=True)
    last_trained = models.DateField()
    email = models.EmailField()
    ANDi_level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)])
    company_role = models.CharField(choices = company_role_choices, max_length=50)
    img = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.club} - {self.last_trained}'

class Workshop(models.Model):
    name = models.CharField(max_length=50)
    trainers = models.ManyToManyField(
        Trainer, blank=True, through='Workshop_Details')

    def __str__(self):
        return f'{self.name}'


class Workshop_Details(models.Model):
    workshop_name = models.CharField(max_length=50)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)
    experience_level = models.CharField(choices = experience_level, max_length=50)
    
    class Meta:
        verbose_name_plural = 'Workshop_Details'
        unique_together = [[ 'trainer', 'workshop']]

    def __str__(self):
        return f'{self.trainer.name} - {self.workshop} - {self.experience_level}'