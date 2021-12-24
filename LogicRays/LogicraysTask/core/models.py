from django.db import models
from django.db import models
from users.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    STUDENT = 1
    TEACHER = 2
    SUPERVISOR = 3
    ROLE_CHOICES = (
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
        (SUPERVISOR, 'Supervisor'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)


    def __str__(self): 
        return self.user.email

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Product(models.Model):
    category = models.CharField(max_length=30, blank=True)
    brand  = models.CharField(max_length=30, blank=True)
    name = models.CharField(max_length=30, blank=True)
    price =models.IntegerField()
    qty = models.IntegerField()
    product_image = models.ImageField(upload_to='media', blank=True, null=False)

    def __str__(self):
        return self.name

class Order(models.Model):
    timstamp = models.DateTimeField(auto_now = True,blank =True)
    placed = models.BooleanField(default = False)
    total_price = models.IntegerField()
    total_qty = models.IntegerField()
    product = models.ManyToManyField(Product, blank= True)

    def __str__(self):
        return f'{self.total_price} and {self.total_qty}'
    

