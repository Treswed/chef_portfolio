import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chef_site.settings')
django.setup()

from portfolio.models import ChefProfile, Testimonial
from recipes.models import Category, Recipe
from django.contrib.auth.models import User

# Create superuser
print("Creating admin user...")
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@chef.com', 'admin123')
    print("✓ Admin user created (username: admin, password: admin123)")
else:
    print("- Admin user already exists")

# Create Chef Profile
print("\nCreating chef profile...")
chef, created = ChefProfile.objects.get_or_create(
    name="Chef Alessandro Rossi",
    defaults={
        'tagline': "Passionate Chef &amp; Culinary Artist",
        'bio': """Welcome to my culinary world! I'm Chef Alessandro Rossi, a passionate chef with over 15 years of experience in creating exceptional dining experiences. My journey began in the heart of Italy, where I learned the art of traditional cooking from my grandmother.

After training at the prestigious Culinary Institute of Florence, I've had the privilege of working in Michelin-starred restaurants across Europe. My cooking philosophy combines time-honored techniques with modern innovation, always focusing on fresh, seasonal ingredients.

Today, I'm excited to share my recipes, techniques, and love for food with you through this platform. Whether you're a beginner or an experienced cook, I hope to inspire you to create delicious meals and discover the joy of cooking.""",
        'email': 'chef@alessandro.com',
        'phone': '+39 123 456 7890',
        'instagram': 'https://instagram.com/chefalessandro',
        'facebook': 'https://facebook.com/chefalessandro',
        'youtube': 'https://youtube.com/chefalessandro',
        'years_experience': 15,
        'specialties': 'Italian Cuisine, Pasta Making, Mediterranean Dishes, Desserts, Wine Pairing',
    }
)
if created:
    print("✓ Chef profile created")
else:
    print("- Chef profile already exists")

# Create Testimonials
print("\nCreating testimonials...")
testimonials_data = [
    {
        'name': 'Maria Johnson',
        'role': 'Home Cook',
        'content': 'Chef Alessandro\'s recipes are absolutely amazing! I tried his homemade pasta recipe and my family couldn\'t stop raving about it. The instructions are clear and easy to follow.',
        'rating': 5,
        'is_featured': True,
    },
    {
        'name': 'David Chen',
        'role': 'Food Blogger',
        'content': 'I\'ve been following Chef Alessandro for years. His attention to detail and passion for cooking really shows in every recipe. Highly recommended!',
        'rating': 5,
        'is_featured': True,
    },
    {
        'name': 'Sophie Martin',
        'role': 'Cooking Enthusiast',
        'content': 'The cooking videos are so helpful! I love how Chef Alessandro explains each step. I\'ve learned so much about Italian cuisine.',
        'rating': 5,
        'is_featured': True,
    },
    {
        'name': 'James Wilson',
        'role': 'Restaurant Owner',
        'content': 'Professional techniques made accessible. Chef Alessandro has a gift for teaching. His recipes have inspired several dishes on our menu.',
        'rating': 5,
        'is_featured': True,
    },
    {
        'name': 'Emma Thompson',
        'role': 'Culinary Student',
        'content': 'As a culinary student, I find Chef Alessandro\'s content incredibly valuable. The tips and tricks have really improved my cooking skills.',
        'rating': 5,
        'is_featured': True,
    },
    {
        'name': 'Michael Brown',
        'role': 'Home Chef',
        'content': 'The best cooking resource I\'ve found online. Every recipe I\'ve tried has turned out perfectly. Thank you, Chef Alessandro!',
        'rating': 5,
        'is_featured': True,
    },
]

for testimonial_data in testimonials_data:
    testimonial, created = Testimonial.objects.get_or_create(
        name=testimonial_data['name'],
        defaults=testimonial_data
    )
    if created:
        print(f"✓ Created testimonial from {testimonial_data['name']}")

# Create Recipe Categories
print("\nCreating recipe categories...")
categories_data = [
    {'name': 'Appetizers', 'icon': '🥗', 'description': 'Start your meal right'},
    {'name': 'Main Courses', 'icon': '🍝', 'description': 'Hearty and satisfying dishes'},
    {'name': 'Desserts', 'icon': '🍰', 'description': 'Sweet endings'},
    {'name': 'Pasta', 'icon': '🍜', 'description': 'Traditional Italian pasta dishes'},
    {'name': 'Soups', 'icon': '🍲', 'description': 'Warm and comforting'},
    {'name': 'Salads', 'icon': '🥙', 'description': 'Fresh and healthy'},
]

for cat_data in categories_data:
    category, created = Category.objects.get_or_create(
        name=cat_data['name'],
        defaults=cat_data
    )
    if created:
        print(f"✓ Created category: {cat_data['name']}")

# Create Sample Recipes
print("\nCreating sample recipes...")
recipes_data = [
    {
        'title': 'Classic Spaghetti Carbonara',
        'description': 'An authentic Roman pasta dish made with eggs, cheese, pancetta, and black pepper. Simple yet incredibly delicious.',
        'category': 'Pasta',
        'prep_time': 10,
        'cook_time': 20,
        'servings': 4,
        'difficulty': 'medium',
        'ingredients': '''400g spaghetti
200g pancetta or guanciale, diced
4 large eggs
100g Pecorino Romano cheese, grated
Black pepper, freshly ground
Salt for pasta water''',
        'instructions': '''Bring a large pot of salted water to boil and cook spaghetti according to package directions.
While pasta cooks, fry pancetta in a large pan until crispy.
In a bowl, whisk together eggs, grated cheese, and plenty of black pepper.
Reserve 1 cup of pasta water, then drain the spaghetti.
Remove pan from heat, add hot pasta to the pancetta.
Quickly stir in the egg mixture, adding pasta water to create a creamy sauce.
Serve immediately with extra cheese and black pepper.''',
        'is_featured': True,
    },
    {
        'title': 'Margherita Pizza',
        'description': 'The queen of pizzas with fresh mozzarella, tomato sauce, and basil. A true Italian classic.',
        'category': 'Main Courses',
        'prep_time': 120,
        'cook_time': 15,
        'servings': 2,
        'difficulty': 'medium',
        'ingredients': '''For the dough:
500g flour
325ml warm water
7g active dry yeast
2 tsp salt
1 tbsp olive oil

For the topping:
400g crushed tomatoes
250g fresh mozzarella
Fresh basil leaves
Extra virgin olive oil
Salt''',
        'instructions': '''Mix yeast with warm water and let sit for 5 minutes.
Combine flour and salt, add yeast mixture and olive oil.
Knead for 10 minutes until smooth and elastic.
Let dough rise for 2 hours until doubled.
Preheat oven to maximum temperature (250°C/480°F).
Roll out dough into thin circles.
Spread tomato sauce, add torn mozzarella.
Bake for 10-15 minutes until crust is golden.
Top with fresh basil and drizzle with olive oil.''',
        'is_featured': True,
    },
    {
        'title': 'Tiramisu',
        'description': 'The iconic Italian dessert with layers of coffee-soaked ladyfingers and mascarpone cream.',
        'category': 'Desserts',
        'prep_time': 30,
        'cook_time': 0,
        'servings': 8,
        'difficulty': 'easy',
        'ingredients': '''6 egg yolks
150g sugar
500g mascarpone cheese
300ml strong espresso, cooled
3 tbsp coffee liqueur (optional)
300g ladyfinger biscuits
Cocoa powder for dusting''',
        'instructions': '''Whisk egg yolks and sugar until pale and thick.
Fold in mascarpone cheese until smooth.
Mix espresso with coffee liqueur in a shallow dish.
Quickly dip ladyfingers in coffee mixture.
Layer half the soaked ladyfingers in a dish.
Spread half the mascarpone mixture over ladyfingers.
Repeat with remaining ladyfingers and cream.
Refrigerate for at least 4 hours or overnight.
Dust generously with cocoa powder before serving.''',
        'is_featured': True,
    },
]

for recipe_data in recipes_data:
    category = Category.objects.get(name=recipe_data['category'])
    recipe_data['category'] = category
    
    recipe, created = Recipe.objects.get_or_create(
        title=recipe_data['title'],
        defaults=recipe_data
    )
    if created:
        print(f"✓ Created recipe: {recipe_data['title']}")

print("\n✅ Sample data created successfully!")
print("\n📝 Login credentials:")
print("   Admin: username=admin, password=admin123")
print("\n🌐 Access the site at: http://localhost:8000")
print("   Admin panel: http://localhost:8000/admin")