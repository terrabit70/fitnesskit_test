from rest_framework import routers
from service.resources import AppointmentResource

router = routers.DefaultRouter()
router.register(r'appointments', AppointmentResource)
