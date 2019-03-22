from django.db import models

# Create your models here.
from django.db.models import *


class User(models.Model):
    user_id = AutoField(primary_key=True)
    user_name = CharField(max_length=20)
    user_age = IntegerField(default=18)
    user_birthday = DateTimeField()
    user_addr = CharField(max_length=200)
