from django.db import models

# Create your models here.
class Meet(models.Model):
    title = models.CharField(max_length = 50)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title