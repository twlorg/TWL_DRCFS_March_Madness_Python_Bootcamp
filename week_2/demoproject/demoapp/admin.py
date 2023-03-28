from django.contrib import admin
from . import models


admin.site.register(models.TestDb)
admin.site.register(models.NewUser)
admin.site.register(models.UserMedia)