from django.db import models
from django.db.models import F


class Rate(models.Model):
    currency = models.CharField(max_length=5)
    sale = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=70)


class ContactUs(models.Model):
    email_from = models.EmailField()
    subject = models.CharField(max_length=120)
    message = models.TextField()


class Options(models.Model):
    b = models.BooleanField(default=True)
    datetime_add = models.DateTimeField(auto_now_add=True)
    datetime_saved = models.DateTimeField(auto_now=True)
    duration = models.DurationField()
    duration.db_index = True

    duration2 = models.GeneratedField(
        expression=F("datetime_saved") - F("datetime_add"),
        output_field=models.DurationField(),
        db_persist=True)
