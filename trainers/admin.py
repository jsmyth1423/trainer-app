from django.contrib import admin
from .models import Trainer, Club, Workshop, Workshop_Details
# Register your models here.

admin.site.register(Trainer)
admin.site.register(Club)
admin.site.register(Workshop)
admin.site.register(Workshop_Details)