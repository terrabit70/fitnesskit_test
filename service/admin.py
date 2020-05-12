from django.contrib import admin

from service.models import (
    Appointment,
    Place,
    Service,
    Teacher
)

admin.site.register(Appointment)
admin.site.register(Place)
admin.site.register(Service)
admin.site.register(Teacher)
