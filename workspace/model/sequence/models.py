from django.db import models

from model.models import Period


# Create your models here.
class sequence(Period):
    seq_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.seq_name

    class Meta:
        db_table = "sequence"