from django.shortcuts import render
from .models import Student
from rest_framework.parsers import JSONParser
import io
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from .serializers import StudentSerializers
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def student_create(request):
	if request.method == 'POST':
		json_data = request.body
		stream  = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)
		serializer = StudentSerializers(data = pythondata)
		if serializer.is_valid():
			serializer.save()
			res = {'msg': 'Data Created'}
			json_data = JSONRenderer().render(res)
			return HttpResponse(json_data, content_type = 'application/json')
		json_data = JSONRenderer().render(serializer.errors)
		return HttpResponse(json_data,content_type = 'application/json')
# Create your views here.
