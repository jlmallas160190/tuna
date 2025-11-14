from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import Person


class Patient(Person):
    is_delete = models.BooleanField()

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"


class MedicalSpeciality(models.Model):
    code = models.CharField(_("Código"))
    name = models.CharField(
        _("Nombre"),
    )
    description = models.TextField(_("Descripción"))
    is_active = models.BooleanField()


class Doctor(Person):
    medical_speciality = models.ForeignKey(MedicalSpeciality, on_delete=models.CASCADE)
    is_delete = models.BooleanField()

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"


class Schedule(models.Model):
    day = models.CharField(
        _("Día de la semana"),
    )
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField(blank=True, null=True)
    duration = models.IntegerField()
    is_active = models.BooleanField()


class Availability(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField(blank=True, null=True)
    is_available = models.BooleanField()
    reason = models.CharField(max_length=100)


class Appointment(models.Model):
    PENDING = "PENDING"
    CONFIRM = "CONFIRM"
    CANCEL = "CANCEL"
    COMPLETED = "COMPLETED"
    STATUS = (
        (PENDING, "Pendiente"),
        (CONFIRM, "Confirmada"),
        (CANCEL, "Cancelada"),
        (COMPLETED, "Completeda"),
    )
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    availability = models.ForeignKey(Availability, on_delete=models.CASCADE)
    reason = models.CharField(max_length=100)
    status = models.CharField(
        _("estado"),
        choices=STATUS,
        max_length=50,
        default=PENDING,
    )
