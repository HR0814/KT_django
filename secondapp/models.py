from calendar import month
from django.db import models

class Curriculum(models.Model):
    name = models.CharField(max_length=255)

    # 오버라이딩 overriding
    def __str__(self) -> str:
        return '@@@' + self.name


class Course(models.Model):
    name = models.CharField(max_length=30)
    cnt = models.IntegerField()

class ArmyShop(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    type = models.IntegerField
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'Army_Shop'

        managed = False
