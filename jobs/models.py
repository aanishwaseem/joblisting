from django.db import models

# Create your models here.
class Jobs(models.Model):
    JOB_TYPE = [
        ('ML', 'Machine Learning'),
    ]
    id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=2, choices=JOB_TYPE)

    def __str__(self):
        return self.title