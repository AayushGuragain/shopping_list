from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
    item_name = models.CharField(max_length = 300)
    description = models.TextField(null=True, blank=True)
    purchased = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.item_name

    class Meta:
        '''
        Orders items based on if they are purchased, and then if they are not, when they are created. The first creation is prioritized.
        '''
        ordering = ['purchased', 'created']
