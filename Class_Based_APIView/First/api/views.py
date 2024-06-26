from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class student_api(APIView):

	def get(self, request, pk = None, format = None):
		id = pk
		if id is not None:
			stu = Student.objects.get(id = id)
			serializer = StudentSerializer(stu)
			return Response(serializer.data)
		stu = Student.objects.all()
		serializer = StudentSerializer(stu, many = True)
		return Response(serializer.data)

	def post(self, request, format = None):
		data = request.data
		serializer = StudentSerializer(data = data)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'Data Inserted !! '}, status = status.HTTP_201_CREATED)
		return Response(serializer.errors)


	def put(self, request, pk , format = None):
		id = pk
		stu = Student.objects.get(id=id)
		serializer = StudentSerializer(stu, data= request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg': 'Data Updated !!!'}, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

	def patch(self, request, pk , format = None):
		id = pk 
		stu = Student.objects.get(id = id)
		serializer = StudentSerializer(stu, data = request.data, partial = True)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'Data Updated !!!'})
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


	def delete(self, request, pk, format = None):
		id = pk
		stu = Student.objects.get(id = id)
		stu.delete()
		return Response({'msg':'Data Deleted ! '})


	


