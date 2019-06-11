from django.contrib import admin

from . import models
# Register your models here.

for model in models.PERMISSION_MODELS:
    admin.site.register(getattr(models, model))
