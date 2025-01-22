from datetime import datetime, timedelta

from django.db import models


class Session(models.Model):
    title = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0.00)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    max_clients = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['-date', '-start_time', '-end_time']

    @property
    def duration(self) -> str:
        start = datetime.combine(self.date, self.start_time)
        end = datetime.combine(self.date, self.end_time)
        duration = end - start
        total_seconds = int(duration.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        if hours > 0:
            if minutes > 0:
                return f"{hours}h {minutes}min"
            else:
                return f"{hours}h"
        else:
            return f"{minutes}min"

    @property
    def available_slots(self) -> int:
        return self.max_clients
