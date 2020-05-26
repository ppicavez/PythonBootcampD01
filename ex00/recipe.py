class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients,
                 recipe_type, description="No description"):
        if not isinstance(name, str):
            print("Name should be a string")
            return
        if name == "":
            print("Name should be not empty")
            return
        if not isinstance(cooking_lvl, int):
            print("Cooking level should be an unsigned integer")
            return
        else:
            cooking_lvl = int(cooking_lvl)
            if cooking_lvl < 0 or cooking_lvl > 5:
                print("Cooking level should be between 1 and 5 (included)")
                return
        if not isinstance(cooking_time, int):
            print("Cooking time should be a positive integer")
            return
        else:
            cooking_time = int(cooking_time)
            if cooking_time <= 0:
                print("Cooking time should be a positive integer")
                return
        if not ingredients:
            print("Ingredients should not be empty")
            return
        elif not isinstance(ingredients, list):
            print("Ingredients should be a list")
        if not isinstance(recipe_type, str):
            print("Recipe type should be a string")
            return
        elif recipe_type not in ["starter", "lunch", "dessert"]:
            print("Choose recipe type in 'starter', 'lunch' or 'dessert'")
            return
        # All is ok
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.recipe_type = recipe_type
        self.description = description

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = "Name: {}\nCooking level: {}\nCooking time: {}\n\
                Ingredients: {}\nRecipe type: {}\nDescription: {}".format(
                self.name, self.cooking_lvl, self.cooking_time,
                self.ingredients,
                self.recipe_type, self.description)
        return txt
