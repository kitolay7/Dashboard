from django.db import models

# Create your models here.
class Hostname(models.Model):
    ip_adress = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)

    def __unicode__(self):
        return "{0} [{1}]".format(self.ip_adress, self.ip)