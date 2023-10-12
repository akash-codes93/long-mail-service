from django.conf.urls import include
from django.urls import path
from long_mail_service.views import (ParcelRetrieveAPIView, TrainRetrieveAPIView, ScheduleAPIView)

urlpatterns = [
    path('parcel/<int:pk>/', ParcelRetrieveAPIView.as_view(), name='parcel-get'),
    path('parcel/', ParcelRetrieveAPIView.as_view(), name='parcel-create'),
    path('train/<int:pk>/', TrainRetrieveAPIView.as_view(), name='parcel-get'),
    path('train/', TrainRetrieveAPIView.as_view(), name='parcel-create'),
    path('schedule/', ScheduleAPIView.as_view(), name='schedule'),
]
