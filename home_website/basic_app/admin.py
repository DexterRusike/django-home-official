from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.HomeBooksToRead)
admin.site.register(models.HomeEvents)
admin.site.register(models.HomeGoals)
admin.site.register(models.HomeTimesheet)
admin.site.register(models.HomeGroceries)


