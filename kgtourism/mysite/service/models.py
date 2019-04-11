import datetime

from django.db import models
from django.utils import timezone


class Hotel(models.Model):
    Address = models.CharField(max_length=200)
    Number = models.IntegerField()
    Staff_of_hotel = models.CharField(max_length=1000)
    Price = models.FloatField()
    Feedback = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.Address, self.Number, self.Staff_of_hotel, self.Price, self.Feedback

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Hostel(models.Model):
    Address = models.CharField(max_length=200)
    Number = models.IntegerField()
    Feedback = models.CharField(max_length=1000)
    Price = models.FloatField()
    Staff_of_hostel = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.Address, self.Number, self.Staff_of_hostel, self.Price, self.Feedback

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Cafe(models.Model):
    Address = models.CharField(max_length=200)
    Number = models.IntegerField()
    Menu = models.CharField(max_length=100)
    Feedback = models.CharField(max_length=1000)
    Price = models.FloatField()
    Staff_of_cafe = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.Address, self.Number, self.Menu, self.Staff_of_cafe, self.Price, self.Feedback

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Attraction(models.Model):
    Address = models.CharField(max_length=200)
    Number = models.IntegerField()
    Feedback = models.CharField(max_length=1000)
    Price = models.FloatField()
    Staff_of_attraction = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.Address, self.Number, self.Staff_of_attraction, self.Price, self.Feedback

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Regions (models.Model):
    REGION_NAME = (
        (1,'Issyk-Kul'),
        (2,'Naryn'),
        (3,'Chuy'),
        (4,'Osh'),
        (5,'Batken'),
        (6,'Zhalal-Abad'),
        (7,'Talas')
    )

    def __str__(self):
        return self.REGION_NAME

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Staff_of_hotel(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    Name = models.CharField(max_length=200)
    Surname = models.CharField(max_length=300)
    Assessment = models.IntegerField(max_length=100)

    def __str__(self):
        return self.hotel, self.Name, self.Surname,self.Assessment


class Staff_of_hostel(models.Model):
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    Name = models.CharField(max_length=200)
    Surname = models.CharField(max_length=300)
    Assessment = models.IntegerField(max_length=100)

    def __str__(self):
        return self.hostel, self.Name, self.Surname,self.Assessment


class Staff_of_cafe(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    Name = models.CharField(max_length=200)
    Surname = models.CharField(max_length=300)
    Assessment = models.IntegerField(max_length=100)

    def __str__(self):
        return self.cafe, self.Name, self.Surname,self.Assessment


class Staff_of_attraction(models.Model):
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)
    Name = models.CharField(max_length=200)
    Surname = models.CharField(max_length=300)
    Assessment = models.IntegerField(max_length=100)

    def __str__(self):
        return self.attraction, self.Name, self.Surname,self.Assessment