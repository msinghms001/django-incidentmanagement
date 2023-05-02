from django.contrib import admin
from .models import Incidents


@admin.register(Incidents)
class IncAdmin(admin.ModelAdmin):
    list_display=['id','reporter','status','priority','reportedOn']
    list_filter=['reporter']