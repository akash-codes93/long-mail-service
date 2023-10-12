from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from long_mail_service.api import *
from long_mail_service.service.serializers import *


class ParcelRetrieveAPIView(generics.CreateAPIView, generics.RetrieveAPIView):

    serializer_class = ParcelSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        parcel_data = ParcelAPI.create_parcel(**serializer.data)
        return Response(parcel_data, status=status.HTTP_201_CREATED)


    def retrieve(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        details = ParcelAPI.get_parcel_details(pk)
        return Response(details)


class TrainRetrieveAPIView(generics.CreateAPIView, generics.RetrieveAPIView):

    serializer_class = TrainSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        train_data = TrainAPI.create_train(**serializer.data)
        return Response(train_data, status=status.HTTP_201_CREATED)


    def retrieve(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        details = TrainAPI.get_train_details(pk)
        return Response(details)


class ScheduleAPIView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        schedule = PostMasterAPI.schedule_parcel()
        return Response(schedule, status=status.HTTP_200_OK)
