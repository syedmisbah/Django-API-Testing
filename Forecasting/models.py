from django.db import models as models


class BaseTable(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    CustomerID = models.IntegerField()
    Account = models.TextField(max_length=100)

