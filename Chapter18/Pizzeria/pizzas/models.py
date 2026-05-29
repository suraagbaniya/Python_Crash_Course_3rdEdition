from django.db import models

# Create your models here.

class Pizza(models.Model):
    """ Pizza model to hold information about pizza """
    text = models.CharField(max_length=50)
    
    def __str__(self):
        return self.text
    
class Topping(models.Model):
    """Toppings that go in a pizza """
    pizza = models.ForeignKey(Pizza, on_delete = models.CASCADE)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
