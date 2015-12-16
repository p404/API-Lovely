from django.db import models
import random
import time


class Listing(models.Model):
    price = models.IntegerField(blank=False, null=False)
    beds = models.IntegerField(blank=False, null=False)
    baths = models.IntegerField(blank=False, null=False)
    address = models.CharField(blank=False, null=False, max_length=120)
    provider_name = models.CharField(blank=False, null=False, max_length=120)

    class Meta:
        ordering = ('price',)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        # it takes time to add new inventory, anywhere from 5 to 15 seconds
        computational_wait = random.randrange(5, 15)
        time.sleep(computational_wait)

        return super().save(force_insert, force_update, using, update_fields)
