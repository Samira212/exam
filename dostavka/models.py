from django.contrib.auth.models import User
from django.db import models



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField(default=0)
    date_registered = models.DateTimeField(auto_now_add=True)
    email = models.EmailField( null=True, blank=True)
    phone_number = models.PositiveSmallIntegerField(default=0)
    STATUS_CHOICES = (
        ('gold', 'gold'),
        ('silver', 'silver'),
        ('bronze', 'bronze'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='bronze')



class Category(models.Model):
    cafget_name = models.CharField(max_length=100)



class Food(models.Model):
    resto_name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ManyToManyField(Category, related_name='категория')
    image = models.ImageField()
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.resto_name


class Courier(models.Model):
    courier_name = models.CharField(max_length=100)
    phone_number = models.IntegerField(default=0)
    STATUS_CHOICES = (
        ('car', 'car'),
        ('bike', 'bike'),
        ('walk', 'walk')
    )

    status = models.CharField(max_length=16, choices=STATUS_CHOICES)



class Order(models.Model):
    order_number = models.IntegerField(default=0)
    resto_name = models.ForeignKey(Food, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    delivery_time = models.DateField()
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)




class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('Доставлен', 'Доставлен'),
        ('В пути', 'В пути'),
        ('Обработка', 'Обработка'),
    )

    status = models.CharField(max_length=100, choices=STATUS_CHOICES)




class Rating(models.Model):
    resto_name = models.ForeignKey(Food, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name="Rating")



class Review(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    resto = models.ForeignKey(Food, on_delete=models.CASCADE)
    parent_review = models.ForeignKey('self', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=True)







