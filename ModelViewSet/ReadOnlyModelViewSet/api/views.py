from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets




class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):

	queryset = Student.objects.all()
	serializer_class = StudentSerializer
	

