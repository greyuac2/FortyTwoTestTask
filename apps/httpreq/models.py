from django.db import models


class HttpReqStore(models.Model):
    id = models.AutoField(primary_key=True)
    htresponce = models.TextField()
    atime = models.DateTimeField(auto_now_add=True)
