from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer

class PatientDoctorMappingViewSet(viewsets.ModelViewSet):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]
    
    @action(detail=False, methods=['get'], url_path='patient/(?P<patient_id>[^/.]+)')
    def get_patient_doctors(self, request, patient_id=None):
        try:
            mappings = PatientDoctorMapping.objects.filter(patient_id=patient_id)
            serializer = self.get_serializer(mappings, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({
                'error': 'Failed to retrieve patient doctors',
                'details': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)