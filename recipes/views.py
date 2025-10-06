from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Avg
from .models import Recipe, Category, RecipeRating

def recipe_list(request):
    recipes = Recipe.objects.all()
    categories = Category.objects.all()
    
    # Search
    search_query = request.GET.get('search', '')
    if search_query:
        recipes = recipes.filter(
            Q(title__icontains=search_query) | 
            Q(description__icontains=search_query)
        )
    
    # Filter by category
    category_slug = request.GET.get('category', '')
    if category_slug:
        recipes = recipes.filter(category__slug=category_slug)
    
    # Filter by difficulty
    difficulty = request.GET.get('difficulty', '')
    if difficulty:
        recipes = recipes.filter(difficulty=difficulty)
    
    context = {
        'recipes': recipes,
        'categories': categories,
        'search_query': search_query,
        'selected_category': category_slug,
        'selected_difficulty': difficulty,
    }
    return render(request, 'recipes/recipe_list.html', context)

def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    recipe.views += 1
    recipe.save()
    
    ratings = recipe.ratings.all()
    avg_rating = ratings.aggregate(Avg('rating'))['rating__avg'] or 0
    
    # Handle rating submission
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        rating = request.POST.get('rating')
        comment = request.POST.get('comment', '')
        
        RecipeRating.objects.create(
            recipe=recipe,
            name=name,
            email=email,
            rating=rating,
            comment=comment
        )
    
    context = {
        'recipe': recipe,
        'ratings': ratings,
        'avg_rating': round(avg_rating, 1),
        'rating_count': ratings.count(),
    }
    return render(request, 'recipes/recipe_detail.html', context)