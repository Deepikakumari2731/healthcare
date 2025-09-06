from rest_framework import serializers
from .models import PatientDoctorMapping
from patients.serializers import PatientSerializer
from doctors.serializers import DoctorSerializer

class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    patient_details = PatientSerializer(source='patient', read_only=True)
    doctor_details = DoctorSerializer(source='doctor', read_only=True)
    
    class Meta:
        model = PatientDoctorMapping
        fields = '__all__'
        read_only_fields = ('assigned_date',)
    
    def validate(self, attrs):
        patient = attrs['patient']
        doctor = attrs['doctor']
        
        # Check if mapping already exists
        if PatientDoctorMapping.objects.filter(patient=patient, doctor=doctor).exists():
            raise serializers.ValidationError("This patient is already assigned to this doctor.")
        
        return attrs