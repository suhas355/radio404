
from django.db import models
from django.contrib.auth.models import User


class Track(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=None)
    url = models.CharField(max_length=400, null=False, unique=True)
    title = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    up_count = models.IntegerField(default=0)
    down_count = models.IntegerField(default=0)

    def __unicode__(self):
        return u"%s" %(self.title)
