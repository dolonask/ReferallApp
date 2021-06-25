from django.db import models

from datetime import datetime

# Create your models here.

invite_statuses = (
    ('ACTIVE', 'Активна'),
    ('NOT_ACTIVE', 'Неактивна'),
    ('ACCEPTED', 'Принята'),
)


# 31.12.2999

class Subscriber(models.Model):
    subs_id = models.IntegerField(primary_key=True)
    phone = models.CharField(max_length=20)
    add_date = models.DateTimeField(auto_now_add=True)  # insert
    edit_date = models.DateTimeField(auto_now=True)  # update
    active = models.BooleanField(default=True)


class Invite(models.Model):
    sender = models.ForeignKey(Subscriber, on_delete=models.DO_NOTHING, related_name="senders")
    receiver = models.ForeignKey(Subscriber, on_delete=models.DO_NOTHING, related_name="receivers")
    status = models.CharField(max_length=20, choices=invite_statuses)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(default=datetime(2999, 12, 31))
