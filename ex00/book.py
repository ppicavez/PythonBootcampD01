from recipe import Recipe
from datetime import datetime


class Book:
    def __init__(self, name):
        if not name:
            print("Name should not be empty")
            return
        self.name = name
        self.recipe_list = {'starter': [], 'lunch': [], 'dessert': []}
        self.creation_date = datetime.now()
        # At the begining by convention, last_update = creation_date
        self.last_update = self.creation_date

    def add_recipe(self, recipe):
        """Add a new recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            print("Second parameter should be a recipes object")
            return
        # All is OK
        self.recipe_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()

    def get_recipe_by_name(self, name):
        """Print a recipe whose name is `name` and print the datas"""
        for k in self.recipe_list:
            for i in self.recipe_list[k]:
                if name in i.name:
                    print(i)

    def get_recipes_by_types(self, recipe_type):
        """Print all recipe names for a given recipe_type"""
        for k in self.recipe_list:
            if k in recipe_type:
                print(self.recipe_list[k])
