from django.contrib import admin
from .models import CarModel, CarMake

# Register your models here.

# CarModelInline class
admin.site.register(CarModel)
# CarModelAdmin class

# CarMakeAdmin class with CarModelInline
admin.site.register(CarMake)
# Register models here
