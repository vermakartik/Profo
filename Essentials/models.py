from django.db import models

# Create your models here.
MAX_LENGTH_SINGLES = 256
class CategoryCasteModel(models.Model):
    caste_name = models.CharField(max_length=MAX_LENGTH_SINGLES)
    caste_code = models.CharField(max_length=3)

    def __str__(self):
        return "" + str(self.caste_name) + "-" + str(self.caste_code)