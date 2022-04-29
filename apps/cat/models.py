from email.policy import default
import uuid

from django.db import models
from django.contrib.auth import get_user_model

from phonenumber_field.modelfields import PhoneNumberField


User = get_user_model()


class Cat(models.Model):
    uuid = models.UUIDField(verbose_name="UUID", default=uuid.uuid4, unique=True)
    title = models.CharField(verbose_name="Title", max_length=50)
    description = models.TextField(verbose_name="Description *необязательное поле", max_length=500, blank=True, null=True)
    image = models.ImageField(verbose_name="Image *необязательное поле", upload_to="cats_images", blank=True, default="default_cat.png")
    breed = models.CharField(verbose_name="Breed", max_length=150)
    birth_date = models.DateField(verbose_name="Date of birth")
    location = models.CharField(verbose_name="Location", max_length=200)
    owner = models.ForeignKey(User, verbose_name="Owner", related_name='cat', on_delete=models.CASCADE)
    contact_number = PhoneNumberField(verbose_name="Contact Number")
    price = models.DecimalField(verbose_name="Price in $", max_digits=8, decimal_places=0)
    added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Кот"
        verbose_name_plural = "Коты"

    def __str__(self):
        return self.title
