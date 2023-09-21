from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from .serializers import InstructorSerializer
from .import models
class InstructorList(generics.ListCreateAPIView):
     queryset=models.Instructor.objects.all()
     serializer_class=InstructorSerializer      
     permission_classes=[permissions.IsAuthenticated]

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
     queryset=models.Instructor.objects.all()
     serializer_class=InstructorSerializer
     permission_classes=[permissions.IsAuthenticated]
