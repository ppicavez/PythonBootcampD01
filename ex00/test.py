from book import Book
from recipe import Recipe

# tests for recipe object
recipe_with_error = Recipe("Fish&chips", -1, 60, ["Fish", "Chips"], "lunch",
                           "")
recipe_with_error = Recipe("", -1, 60, ["Nothing", "Nothing"], "dessert", "")
recipe_with_error = Recipe("Apple pie", "NaN", 30, ["Apples", "floor", "eggs",
                           "butter"], "dessert", "")
recipe_with_error = Recipe("Chocalate cake", -1, 60,
                           ["Chocolate", "floor", "eggs", "butter"],
                           "dessert", "")
recipe_with_error = Recipe(" Strawberry pie", 1, -50, ["Strawberry",
                           "floor", "eggs", "butter"], "dessert", "")
recipe_with_error = Recipe(" Kidney pie", 6, 50, ["Strawberry", "floor",
                           "eggs", "butter"], "starter", "No comment")
recipe_with_error = Recipe(" Strawberry pie", 1, 50, "False list",
                           "dessert",
                           "")
recipe_with_error = Recipe(" Cofee Ice screem ", 1, 50, ["Cofee", "Ice",
                           "Scream"],
                           "False Type", "")
recipe_with_error = Recipe(" Fried Liver ", 1, 50, ["Liver", "Chessboard"],
                           "", "")

good_recipe1 = Recipe("Lyonnaise salad", 1, 5,
                      ["tomatoes", "eggs", "oil", "ham", "salt", "pepper"],
                      "starter", "The simplest one")
print("______________________________________________________________________")

print(good_recipe1)
good_recipe2 = Recipe("Fish and ships", 1, 60, ["Fish", "potatoes"],
                      "lunch", "")
good_recipe3 = Recipe("New recipe", 2, 60, ["Sugar", "Butter"],
                      "dessert", "")
good_recipe4 = Recipe("Apple pie", 2, 30,
                      ["Apples", "floor", "eggs", "butter"], "dessert", "")
good_recipe5 = Recipe(" Chocalate cake", 3,  60,
                      ["Chocolate", "floor", "eggs", "butter"], "dessert", "")
good_recipe6 = Recipe(" Strawberry pie", 1, 50,
                      ["Strawberry", "floor", "eggs", "butter"], "dessert", "")
good_recipe7 = Recipe(" Kidney pie", 5, 50, ["Kidney", "floor", "eggs",
                      "butter"],
                      "starter", "No comment")
good_recipe8 = Recipe("Cofee Ice screem ", 1, 50,
                      ["Cofee", "Ice", "Scream"], "dessert", "")
good_recipe9 = Recipe("Fried Liver ", 1, 50, ["Liver", "Chessboard"],
                      "lunch", "")
# test for  book object
cookbook = Book("My First CookBook ")
cookbook.add_recipe(good_recipe1)
cookbook.add_recipe(good_recipe2)
cookbook.add_recipe(good_recipe3)
cookbook.add_recipe(good_recipe4)
cookbook.add_recipe(good_recipe5)
cookbook.add_recipe(good_recipe6)
cookbook.add_recipe(good_recipe7)
cookbook.add_recipe(good_recipe8)
cookbook.add_recipe(good_recipe9)
print("______________________________________________________________________")
print(cookbook.get_recipes_by_types("as"))
print("______________________________________________________________________")
print(cookbook.get_recipes_by_types("dessert"))
print("______________________________________________________________________")
print(cookbook.get_recipes_by_types("starter"))
print("______________________________________________________________________")
print(cookbook.get_recipes_by_types("lunch"))
print("______________________________________________________________________")

print(cookbook.get_recipe_by_name("cNotGood"))
print("______________________________________________________________________")
print(cookbook.get_recipe_by_name("Apple pie"))
print("_____________________________________END______________________________")
