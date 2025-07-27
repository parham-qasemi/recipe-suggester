recipes = {
    # Egg-based
    "Omelette": ["egg", "tomato", "salt"],
    "Fried Egg": ["egg", "salt", "oil"],
    "Boiled Egg": ["egg", "water", "salt"],

    # Potato-based
    "Mashed Potatoes": ["potato", "milk", "butter", "salt"],
    "Potato Patties": ["potato", "egg", "onion", "salt"],
    "French Fries": ["potato", "oil", "salt"],

    # Rice-based
    "Plain Rice": ["rice", "salt", "oil", "water"],
    "Vegetable Rice": ["rice", "carrot", "peas", "onion", "salt"],
    "Chicken and Rice": ["rice", "chicken", "onion", "salt", "spices"],

    # Chicken dishes
    "Grilled Chicken": ["chicken", "oil", "salt", "pepper"],
    "Chicken Stew": ["chicken", "onion", "tomato paste", "salt", "spices"],
    "Chicken Salad": ["chicken", "lettuce", "mayonnaise", "carrot"],

    # Beef dishes
    "Spaghetti with Meat Sauce": ["macaroni", "ground beef", "onion", "tomato paste", "salt"],
    "Beef Stew": ["beef", "onion", "carrot", "potato", "salt", "spices"],
    "Kebab": ["ground beef", "onion", "salt", "pepper"],

    # Fish dishes
    "Fried Fish": ["fish", "salt", "pepper", "oil"],
    "Baked Salmon": ["salmon", "lemon", "garlic", "salt", "olive oil"],
    "Tuna Salad": ["canned tuna", "corn", "lettuce", "mayonnaise"],

    # Soups
    "Lentil Soup": ["lentil", "onion", "carrot", "salt", "spices"],
    "Chicken Soup": ["chicken", "carrot", "onion", "noodles", "salt"],
    "Vegetable Soup": ["carrot", "potato", "onion", "peas", "salt", "spices"],

    # Vegetarian
    "Grilled Vegetables": ["zucchini", "eggplant", "pepper", "salt", "olive oil"],
    "Veggie Stir-fry": ["carrot", "pepper", "onion", "soy sauce", "oil"],
    "Spinach Omelette": ["egg", "spinach", "salt"],

    # Persian (Iranian) foods
    "Persian Ash": ["ash noodles", "lentil", "beans", "chickpeas", "onion", "kashk", "dried mint"],
    "Zereshk Polo": ["rice", "barberry", "chicken", "onion", "saffron", "salt"],
    "Kookoo Sabzi": ["egg", "herbs", "salt", "oil"],

    # Snacks / Other
    "Pasta Salad": ["macaroni", "corn", "peas", "mayonnaise"],
    "Tuna Sandwich": ["bread", "canned tuna", "mayonnaise", "lettuce"],
    "Egg Salad": ["egg", "mayonnaise", "lettuce", "salt"],
}


# Welcome message
print("=" * 50)
print("🍽️  Welcome to Recipe Suggester!")
print("👨‍🍳  Enter the ingredients you have (separated by commas):")
print("=" * 50)

# Ask the user to enter available ingredients
user_input = input("Enter the ingredients you have (separated by commas): ")

# Split the input by commas and clean spaces
user_ingredients = [item.strip().lower() for item in user_input.split(",")]



# Create an empty list to store suggested recipes
suggested_recipes = []

# Go through all recipes
for dish, ingredients in recipes.items():
    # Check if all required ingredients are in user's list
    if all(item in user_ingredients for item in ingredients):
        suggested_recipes.append(dish)

# Show results
print("\n" + "-" * 50)
if suggested_recipes:
    print("✅ You can make the following recipes:")
    for recipe in suggested_recipes:
        print("• " + recipe)
else:
    print("❌ Sorry, no matching recipes found.")
print("-" * 50)

