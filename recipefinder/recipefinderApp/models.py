from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    units = models.CharField(max_length=200)
    image = models.ImageField(upload_to='recipe')
    ingredients = models.ManyToManyField('Ingredient')
    servings = models.CharField(max_length=10)
    time = models.IntegerField()
    instructions = models.TextField()
    dietary_requirement = models.CharField(max_length=200)
    cuisine = models.ManyToManyField('Cuisine')
    # likes = models.ManyToManyField('Likes')
    comments = models.ManyToManyField('Comments')
    
    class Meta:
        ordering = ('title',)
    
    def __str__(self):
        return str(self.title).capitalize()

# --------------------- #

class Ingredient(models.Model):
    title = models.CharField(max_length=50)
    ingredient_id = models.IntegerField()

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return str(self.title).capitalize()

# --------------------- #

class Cuisine(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return str(self.name).capitalize()

# --------------------- #

class Comments(models.Model):
    comment = models.CharField(max_length=200)

    class Meta:
        ordering = ('comment',)

    def __str__(self):
        return str(self.comment).capitalize()

# --------------------- #

# class Likes(models.Model):
#     # user = models.ForeignKey(User)
#     recipe = models.ForeignKey(Recipe)
#     timestamp = models.DateTimeField()

#     def __str__(self):
#         return str(self.recipe).capitalize()
