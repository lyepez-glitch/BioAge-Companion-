from django.contrib import admin

# Register your models here.
from .models import HealthMetrics, Recommendations

admin.site.register(HealthMetrics)
admin.site.register(Recommendations)