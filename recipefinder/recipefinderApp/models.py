from django.db import models

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
