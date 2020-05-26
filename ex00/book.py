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

    def get_recipe_by_name(self, name: str) -> object:
        """Print a recipe with the given name and return the instance
        :param name: str, recipe name
        :return: instance of Recipe class instance with a given name (or None)
        """
        # search for a recipe
        result = None
        for recipe_list in self.recipe_list.values():
            if result is None:
                for recipe in recipe_list:
                    if recipe.name == name:
                        result = recipe
                        break
        # return None if recipe not found
        if result is None:
            print(f"Recipe named '{name}' unknown.")
            return
        return result

    def get_recipes_by_types(self, recipe_type: str) -> list:
        """Get all recipe names for a given 'recipe_type'
        :param recipe_type: one of the valid recipe types
        :return: list of names (or empty list on error)
        """
        if not (recipe_type in self.recipe_list.keys()):
            print(f"Recipe type '{recipe_type}' not recognized")
            print(f"Valid recipe types: {', '.join(self.recipe_list.keys())}")
            return []
        names_list = [recipe.name for recipe in self.recipe_list[recipe_type]]
        return names_list

    def add_recipe(self, recipe: Recipe):
        """Add a recipe to the book and update last_update
        :param recipe: Recipe class object
        """
        if not isinstance(recipe, Recipe):
            print(f"{recipe} is not a valid recipe.",
                  "Please, create a valid recipe in official recipe module.")
            return
        self.recipe_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()
