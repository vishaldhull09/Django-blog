from rest_framework import serializers
from .models import Profile



class SampleSerializer(serializers.ModelSerializer):
	class  Meta:

		model = Profile
		fields = "__all__"
		"""docstring for  Meta"""
		