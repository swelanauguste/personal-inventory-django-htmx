from django.db import models

# from django.db.models import Q
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    uid = models.CharField(
        "UID", max_length=100, unique=True, null=True, blank=True, help_text="Unique ID"
    )
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True)
    model = models.CharField(max_length=100, null=True, blank=True)
    memory = models.IntegerField(default=8, help_text="RAM in GB")
    storage = models.IntegerField(default=100, help_text="HDD in GB")
    description = models.TextField(max_length=1000)
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["tags__name", "uid"]

    def get_absolute_url(self):
        return reverse("item-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name
