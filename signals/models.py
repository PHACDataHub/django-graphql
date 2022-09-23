"""
Signal Model
"""
from django.db import models

from signals.i18n.decorators import translate, add_admin


@add_admin()
class Program(models.Model):
    name = models.CharField(max_length=400)

    def __str__(self):
        return f"{self.name}"


@add_admin()
class Contact(models.Model):
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    email = models.CharField(max_length=400)
    program = models.ForeignKey("Program", on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.first_name} {self.last_name} <{self.email}>"


@translate(('name',), admin=True)
class Hazard(models.Model):
    name = models.CharField(max_length=400)

    def __str__(self):
        return f"{self.name}"


@translate(('name', 'description',), admin=True)
class Source(models.Model):
    name = models.CharField(max_length=400)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


@translate(('name', 'definition', 'examples',), admin=True)
class Quality(models.Model):
    name = models.CharField(max_length=400)
    definition = models.TextField()
    examples = models.TextField()

    class Meta:
        verbose_name_plural = "Qualities"

    def __str__(self):
        return f"{self.name}"


class SignalContact(models.Model):
    signal = models.ForeignKey("Signal", on_delete=models.CASCADE)
    contact = models.ForeignKey("Contact", on_delete=models.CASCADE)
    creator = models.BooleanField()
    primary = models.BooleanField()

    class Meta:
        unique_together = [['primary', 'signal'], ['creator', 'signal']]

    def __str__(self):
        return f"{self.signal} -> {self.contact}"


class SignalLocation(models.Model):
    signal = models.ForeignKey("Signal", on_delete=models.CASCADE)
    city = models.ForeignKey("cities_light.City", on_delete=models.RESTRICT)
    date_of_detection = models.DateField()

    def __str__(self):
        return f"{self.signal} -> {self.city}"


@add_admin(admin_options={'filter_horizontal': ('source',)}, inlines=[SignalContact, SignalLocation])
class Signal(models.Model):
    title = models.CharField(max_length=400)
    location = models.ManyToManyField(
        "cities_light.City", through='SignalLocation')
    contact = models.ManyToManyField("Contact", through='SignalContact')
    source = models.ManyToManyField("Source")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"


class Report(models.Model):
    pass
