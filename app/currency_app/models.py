from django.db import models


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
