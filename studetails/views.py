from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import studentsdetails

# Create your views here.
class student_view_set(viewsets.ViewSet):
    def create(self, request):
        studata = request.data
        print(studata)
        name = studata['Name']
        print(name)
        firstname = name[0:3]
        count = studentsdetails.objects.count()
        idno = count + 20000
        regnum = firstname + str(idno)
        studata['Registernumber'] = regnum
        serializer = StudentSerializer(data=studata)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve_mobilenumber(self, request, pk=None):
        stud_det = studentsdetails.objects.get(Mobilenumber=pk)
        serializer = StudentSerializer(stud_det)
        return Response(serializer.data)

    def retrieve_regnumber(self, request, pk=None):
        stud_det = studentsdetails.objects.get(Registernumber=pk)
        serializer = StudentSerializer(stud_det)
        return Response(serializer.data)

