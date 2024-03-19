from django.contrib import admin
from.models import User,Person,Student,Identification_type, city, departament, country


# Register your models here.
admin.site.register(User)
admin.site.register(Person)
admin.site.register(Student)
admin.site.register(Identification_type)
admin.site.register(city)
admin.site.register(departament)
admin.site.register(country)
