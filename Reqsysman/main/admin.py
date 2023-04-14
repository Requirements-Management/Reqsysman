from django.contrib import admin
from .models import Requirement, RequirementType

admin.site.register(Requirement)
admin.site.register(RequirementType)

# Register your models here.
