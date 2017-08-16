from django.db import models
from django.urls import reverse


def my_model_image_upload_to(instance, filename):
    return "{}/{}".format(instance.pk, filename)


class MyModel(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to=my_model_image_upload_to)

    def get_absolute_url(self):
        return reverse('myapp:my-view', args=(self.pk, ))