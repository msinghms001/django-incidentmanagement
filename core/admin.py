from django.contrib import admin
from .models import Incidents


@admin.register(Incidents)
class IncAdmin(admin.ModelAdmin):
    list_display=['id','reporter','details','status','priority','reportedOn','updatedOn']
    list_filter=['reporter']