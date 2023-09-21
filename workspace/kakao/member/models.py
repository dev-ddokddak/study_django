from django.db import models

# Create your models here.


class Member (Period):
    member_email = models.CharField(blank=False, null=False, max_length=50, unique=True)
    member_password = models.CharField(blank=False, null=)