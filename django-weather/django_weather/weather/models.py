from django.db import models

# Model for a city.
class City(models.Model):
    name = models.CharField(max_length=25)

    # String representation of the object.
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'