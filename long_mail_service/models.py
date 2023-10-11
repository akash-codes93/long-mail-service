from django.db import models
from datetime import timedelta


class Parcel(models.Model):
    id = models.BigAutoField(primary_key=True)
    weight = models.IntegerField()
    volume = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'parcels'


class Line(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'lines'


class Train(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=10)
    cost = models.IntegerField()
    weight = models.IntegerField()
    volume = models.IntegerField()
    lines = models.ManyToManyField(Line)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def unit_cost(self):
        density = self.weight // self.volume
        return self.cost // density

    class Meta:
        managed = True
        db_table = 'trains'


class Trip(models.Model):
    id = models.BigAutoField(primary_key=True)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    line = models.ForeignKey(Line, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    @property
    def end_time(self):
        if self.is_completed is True:
            return self.start_time + timedelta(minutes=3)
        return None

    class Meta:
        managed = True
        db_table = 'trips'



class Booking(models.Model):
    parcel = models.ForeignKey(Parcel, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    strategy = models.CharField(max_length=20, null=True)
    cost = models.FloatField()

    class Meta:
        managed = True
        db_table = 'bookings'
