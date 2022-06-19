from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # auto_now --> take a snapeshot every time we save this
    update = models.DateTimeField(auto_now=True)
    # auto_now_add --> only takes a timestamp when we first save or created
    created = models.DateTimeField(auto_now_add=True)

    # string representation
    def __str__(self):
        return str(self.name)
