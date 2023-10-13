from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class HealthCheckView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)
