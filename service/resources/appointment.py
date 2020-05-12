from rest_framework import viewsets
from service.models import Appointment
from service.serializers.appointment import AppointmentSerializer


class AppointmentResource(viewsets.GenericViewSet, viewsets.mixins.ListModelMixin):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
