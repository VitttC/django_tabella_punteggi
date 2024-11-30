from django.contrib import admin
from punti.models import Punti

class ScoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'value']



admin.site.register(Punti, ScoreAdmin)

# Register your models here.
