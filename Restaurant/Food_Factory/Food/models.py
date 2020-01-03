from django.db import models

class Item(models.Model):

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length = 500, default = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS4Y03vu_-s0Hm8NJbdVxFkVFH5Rhi9STNfuz2-PwckMnj5p768&s")