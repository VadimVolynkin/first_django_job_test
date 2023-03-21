from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class Shop(models.Model):
    organization_id = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="shops")
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    index = models.PositiveBigIntegerField()
    is_deleted = models.BooleanField(default=False)
