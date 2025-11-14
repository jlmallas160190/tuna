from rest_framework import serializers

from medical_appointments.models import MedicalSpeciality


class MedicalSpecialitySerializer(serializers.ModelSerializer):

    class Meta:
        model = MedicalSpeciality
        fields = ["id", "code", "name", "description", "is_active"]
