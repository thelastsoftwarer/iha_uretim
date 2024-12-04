from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Parça Modeli
class Part(models.Model):
    name = models.CharField(max_length=100)
    quantity_in_stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name
class Aircraft(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=[
        ('TB2', 'TB2'),
        ('TB3', 'TB3'),
        ('AKINCI', 'AKINCI'),
        ('KIZILELMA', 'KIZILELMA'),
    ])
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# Ürün Modeli
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    parts = models.ManyToManyField(Part, through='ProductPart')

    def __str__(self):
        return self.name


# Ürün-Parça İlişkisi
class ProductPart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    quantity_used = models.IntegerField()

    def __str__(self):
        return f'{self.product.name} - {self.part.name}'




class AircraftPart(models.Model):
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    quantity_used = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['part'],
                name='unique_part_per_aircraft'
            )
        ]


class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class TeamPart(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)

    def clean(self):
        # Takımın parça sorumluluğunu kontrol et
        if self.part.name.lower() not in self.team.name.lower():
            raise ValidationError(f"{self.team.name} takımı {self.part.name} üretemez.")
