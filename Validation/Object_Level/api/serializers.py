from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
	name = serializers.CharField(max_length = 100)
	roll =serializers.IntegerField()
	city =serializers.CharField(max_length = 100)

	def create(self, validated_data):
		return Student.objects.create(**validated_data)

	def update(self, instance, validated_data):
		print(instance.name)
		instance.name = validated_data.get('name',instance.name)
		print(instance.name)
		instance.roll= validated_data.get('roll',instance.roll)
		instance.city = validated_data.get('city',instance.city)
		instance.save()
		return instance

	#Object Level Validation is used for multiple fields 

	def validate(self, data):
		nm = data.get('name')
		ct = data.get('city')
		if nm.lower() == 'nimesh' and ct.lower() != 'lalbandi':
			raise serializers.ValidationError('City must be lalbandi to be inserted ! Check the name in myapp.py')

		return data
		