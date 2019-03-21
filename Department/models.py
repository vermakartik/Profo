from django.db import models

# Create your models here.
class Department(models.Model):
    department_name = models.CharField(max_length =1024, default = "", blank=False, null = False)
    department_code = models.CharField(max_length =100, default = "", blank=False, null = False)
     
    def __str__(self):
        return str(self.department_name) + " - " + str(self.department_code)
