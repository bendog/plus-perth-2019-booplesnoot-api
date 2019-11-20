from django.contrib import admin

from .models import Recipe, Ingredient, Cuisine, Comments

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Cuisine)
admin.site.register(Comments)

