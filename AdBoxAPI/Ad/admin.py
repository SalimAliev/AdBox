from django.contrib import admin

# Register your models here.
from .models import Ad, AdPhoto

admin.site.register(Ad)
admin.site.register(AdPhoto)