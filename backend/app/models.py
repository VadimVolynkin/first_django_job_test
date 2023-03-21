from django.db import models


class Organization(models.Model):
    """Модель Организации"""
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Shop(models.Model):
    """Модель Магазина"""
    organization_id = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="shops")
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    index = models.PositiveBigIntegerField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
