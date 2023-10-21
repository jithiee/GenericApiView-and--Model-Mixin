#===================  GenericApiView and  Model Mixin =========================

from django.shortcuts import render
from . models import Student
from  . serializer import StudentSerializers
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

# Create your views here.

class StudentList(GenericAPIView,ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    
    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
        
class StudentCreate(GenericAPIView,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    
    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)
    
class StudentRetrive(GenericAPIView,RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    
    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    
class StudentUpdate(GenericAPIView,UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers   
    
    def put(self,request,*args, **kwargs):
        return self.update(request,*args,**kwargs)
    
class StudentDelete(GenericAPIView,DestroyModelMixin):
       queryset = Student.objects.all()
       serializer_class = StudentSerializers
       
       def delete(self,request,*args, **kwargs):
           return self.destroy(request, *args, **kwargs)
       
        
    
   