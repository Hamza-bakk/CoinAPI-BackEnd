from datetime import datetime
from django.db import models
from users.models import UserAccount

# Create your models here.

class Alerts(models.Model):
    userId = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    asset = models.TextField(max_length=35)
    current_price = models.IntegerField()
    target_price = models.IntegerField()
    is_open = models.BooleanField(default=True)
    open_date = models.DateTimeField(default=datetime.now)


    