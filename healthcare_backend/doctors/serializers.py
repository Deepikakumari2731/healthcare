from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
    
    def validate_license_number(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("License number must be at least 5 characters.")
        return value
    
    def validate_experience_years(self, value):
        if value < 0 or value > 60:
            raise serializers.ValidationError("Experience years must be between 0 and 60.")
        return value