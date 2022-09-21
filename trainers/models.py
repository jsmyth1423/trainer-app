from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

company_role_choices = [
    ("1", "Product Developer"),
    ("2", "Product Analyst"),
    ("3", "Squad Lead"),
    ("4", "Cloud Engineer"),
    ("5", "Onboarding Coordinator"),

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
    experience_level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    
    class Meta:
        verbose_name_plural = 'Workshop_Details'
        unique_together = [[ 'trainer', 'workshop']]

    def __str__(self):
        return f'{self.trainer.name} - {self.workshop} - {self.experience_level}'