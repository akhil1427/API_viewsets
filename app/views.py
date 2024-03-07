from django.shortcuts import render
from app.models import *
from app.Serializers import *
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
# Create your views here.

class productcurd(ViewSet):

    def list(self,request):
        LPDO=Product.objects.all()
        JDO=ProductSerializer(LPDO,many=True)
        return Response(JDO.data)

    def retrieve(self,request,pk):
        PO=Product.objects.get(pk=pk)
        JDO=ProductSerializer(PO)
        return Response(JDO.data)

    def create(self,request):
        PO=ProductSerializer(data=request.data)
        if PO.is_valid():
            PO.save()
            return Response({'create':'Data is inserted'})
    
    def update(self,request,pk):
        DPO=Product.objects.get(pk=pk)
        JDPO=ProductSerializer(DPO,data=request.data)
        if JDPO.is_valid():
            JDPO.save()
            return Response({'Update':'Data is updated'})
        else:
            return Response({'Update':'Data not is updated'})

    def partial_update(self,request,pk):
        DPO=Product.objects.get(pk=pk)
        JDPO=ProductSerializer(DPO,data=request.data,partial=True)
        if JDPO.is_valid():
            JDPO.save()
            return Response({'Update':'Data is updated'})
        else:
            return Response({'Update':'Data not is updated'})

    def destroy(self,request,pk):
        Product.objects.get(pk=pk).delete()
        return Response({'Delete':'Data is deleted'})

            
