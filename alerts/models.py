from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model


class Alerts(models.Model):
    userId = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    asset = models.TextField(max_length=35)
    current_price = models.IntegerField()
    target_price = models.IntegerField()
    is_open = models.BooleanField(default=True)
    open_date = models.DateTimeField(default=datetime.now)
    close_date = models.DateTimeField(null=True, blank=True)  # Nouveau champ

    def save(self, *args, **kwargs):
        # Vérifiez si l'alerte vient d'être fermée
        if not self.is_open and self.close_date is None:
            self.close_date = datetime.now()
        super().save(*args, **kwargs)

    