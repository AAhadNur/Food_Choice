from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.Profile)
admin.site.register(models.Restaurant)
admin.site.register(models.Menu)
admin.site.register(models.Vote)
admin.site.register(models.Feedback)
admin.site.register(models.DailyResults)
