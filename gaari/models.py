from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

# Create your models here.

class Make(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to="images", blank=True, null=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name_plural = "Brands"



class Autos(models.Model):
    image = models.ImageField(upload_to="images", null=True)
    nickname = models.CharField(max_length=20, null=True)
    mileage = models.IntegerField( validators=[
        MinValueValidator(1), MaxValueValidator(500000)
    ] )

    comments = models.TextField(max_length=200)
    make = models.ForeignKey('Make', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nickname}"
    
    class Meta:
        verbose_name_plural = "Autos"

class Review(models.Model):
    username = models.CharField(max_length=20)
    content = models.TextField(max_length=100)
    auto = models.ForeignKey("Autos", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username}: {self.content}"

class Message(models.Model):
    sender = models.CharField(max_length=20)
    receiver = models.CharField(max_length=20)
    content = models.TextField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}: {self.created_on}"