from rest_framework import serializers
from . import models
class InstructorSerializer(serializers.ModelSerializer):
     class Meta:
         model=models.Instructor
         fields=['instructorID','firstName','lastName','email','password','dob','address','contactNumber','verificationStatus']
