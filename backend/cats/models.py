from django.db import models
from django.contrib.auth.models import User 

class AboutCats(models.Model):
    age = models.IntegerField()
    breed = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='cat/',blank=True)
    cost = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name} {self.breed}"
    
# class CatsForPeople(models.Model):
#     cat = models.ForeignKey(AboutCats, on_delete=models.CASCADE)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     date = models.DateField(auto_now_add = True)

#     class Meta:
#         unique_together = (("owner","cat"),)

class Balance(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    balance = models.IntegerField(default = 0)

class CatHistory(models.Model):
    buyer = models.ForeignKey(User, on_delete = models.CASCADE)
    seller = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'user_seller')
    cost = models.DecimalField(max_digits = 10, decimal_places = 2)
    cat = models.ForeignKey(AboutCats, on_delete = models.CASCADE)
    date = models.DateField(auto_now_add = True)