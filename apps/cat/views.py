from rest_framework import permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Cat
from .serializers import CatsSerializer

class CatsView(generics.ListAPIView):

    serializer_class = CatsSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Cat.objects.all().order_by("-added")
