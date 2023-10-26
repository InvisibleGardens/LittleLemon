from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)

    class Meta:
        app_label = 'restaurant'

    def __str__(self):
        return f'{self.title} : {str(self.price)}'

    

class Booking(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    number_of_guests = models.PositiveIntegerField()

    def __str__(self):
        return self.name
