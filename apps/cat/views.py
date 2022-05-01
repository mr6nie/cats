from ast import parse
from rest_framework import permissions, generics, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Cat
from .serializers import CatsSerializer, SingleCatSerializer, CreateCatSerializer


class CatsView(generics.ListAPIView):

    serializer_class = CatsSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Cat.objects.all().order_by("-added")


class SingleCatView(viewsets.ModelViewSet):

    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, uuid, *args, **kwargs):
        instance = Cat.objects.get(uuid=uuid)
        serializer = SingleCatSerializer(instance)
        return Response(serializer.data)

    def update(self, request, uuid, *args, **kwargs):
        instance = Cat.objects.get(uuid=uuid)
        serializer = CreateCatSerializer(data=request.data, instance=instance)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def destroy(self, request, uuid, *args, **kwargs):
        instance = Cat.objects.get(uuid=uuid)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class CatCreateView(APIView):

    permission_classes = [permissions.AllowAny]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None, *args, **kwargs):
        serializer = CreateCatSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)