
from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET','POST','PUT','DELETE','PATCH'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def student_api(request,pk=None):

	if request.method == 'GET':
		id = pk
		if id is not None:
			stu = Student.objects.get(id=id)
			serializer = StudentSerializer(stu)
			return Response(serializer.data)

		stu = Student.objects.all()
		serializer = StudentSerializer(stu, many=True)
		return Response(serializer.data)

	if request.method == 'POST':
	 	data = request.data
	 	serializer = StudentSerializer(data = data)
	 	if serializer.is_valid():
	 		serializer.save()
	 		return Response({'msg':'data inserted !'}, status = status.HTTP_201_CREATED)
	 	return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


	if request.method =='PUT':
		id = pk
		stu = Student.objects.get(id=id)
		serializer = StudentSerializer(stu, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'Complete Data Update !'})
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

	if request.method =='PATCH':
		id = pk
		stu = Student.objects.get(id=id)
		serializer = StudentSerializer(stu, data=request.data, partial = True)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'Partial Data Update !'})
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

	if request.method == 'DELETE':
		id = pk
		stu = Student.objects.get(id = id)
		stu.delete()
		return Response({'msg':'Data Deleted ! '})




