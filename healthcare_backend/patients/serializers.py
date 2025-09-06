from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ('created_by', 'created_at', 'updated_at')
    
    def validate_phone(self, value):
        if not value.isdigit() or len(value) < 10:
            raise serializers.ValidationError("Invalid phone number format.")
        return value