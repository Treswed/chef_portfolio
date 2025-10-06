# Chef Portfolio Website

A beautiful Django-based portfolio website for chefs to showcase their recipes, photos, videos, and blog posts. Features cooking-themed animations and a modern, responsive design.

## Features

### 🍳 Core Functionality
- **Recipe Management**: Post recipes with ingredients, instructions, prep/cook times, and difficulty levels
- **Photo Gallery**: Showcase culinary creations with filterable image gallery
- **Video Gallery**: Share cooking videos with embedded players
- **Blog System**: Write articles, stories, and culinary tips
- **Rating System**: Users can rate and review recipes
- **Search & Filter**: Find recipes by category, difficulty, or search terms
- **Responsive Design**: Works perfectly on all devices

### 🎨 Design Features
- **Cooking Animations**: 
  - Floating steam effects
  - Animated cooking utensils (knife, spoon, fork)
  - Falling ingredients (tomato, carrot, onion)
  - Bouncing chef hat logo
- **Modern UI**: Clean, professional design with smooth transitions
- **Color Scheme**: Warm cooking-themed colors (red, orange, yellow)
- **Interactive Elements**: Hover effects, smooth scrolling, lightbox gallery
- **Print-Friendly**: Recipe pages optimized for printing

### 📱 Pages Included
1. **Homepage**: Hero section, featured recipes, stats, testimonials, blog preview
2. **About**: Chef bio, experience timeline, skills showcase
3. **Recipes**: Searchable recipe list with filters
4. **Recipe Detail**: Full recipe with ingredients, instructions, ratings
5. **Gallery**: Photo gallery with category filters
6. **Videos**: Video showcase with thumbnails
7. **Blog**: Blog posts listing and detail pages
8. **Contact**: Contact information and form

## Installation

### Prerequisites
- Python 3.11+
- pip

### Setup Instructions

1. **Navigate to project directory**
   ```bash
   cd chef_portfolio
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations** (Already done)
   ```bash
   python manage.py migrate
   ```

4. **Create sample data** (Already done)
   ```bash
   python create_sample_data.py
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

6. **Access the application**
   - Homepage: http://localhost:8000
   - Admin Panel: http://localhost:8000/admin

## Default Login Credentials

### Admin Account
- **Username**: admin
- **Password**: admin123
- **Access**: Full admin panel access for managing content

## Usage Guide

### For Admins

1. **Login to Admin Panel**
   - Navigate to http://localhost:8000/admin
   - Login with admin credentials

2. **Manage Chef Profile**
   - Go to "Chef Profile" section
   - Update bio, contact info, social media links
   - Upload profile image

3. **Add Recipes**
   - Go to "Recipes" section
   - Click "Add Recipe"
   - Fill in title, description, category, times, difficulty
   - Add ingredients (one per line)
   - Add instructions (one step per line)
   - Upload featured image
   - Optionally add video URL

4. **Manage Gallery**
   - Go to "Gallery Images" section
   - Upload photos with titles and descriptions
   - Categorize images for filtering

5. **Add Videos**
   - Go to "Videos" section
   - Add YouTube or Vimeo URLs
   - Add title, description, and optional thumbnail

6. **Write Blog Posts**
   - Go to "Blog Posts" section
   - Create articles with rich content
   - Upload featured images
   - Publish or save as draft

7. **Manage Testimonials**
   - Go to "Testimonials" section
   - Add customer reviews and ratings
   - Mark featured testimonials for homepage

### For Visitors

1. **Browse Recipes**
   - Navigate to Recipes page
   - Use search bar to find specific recipes
   - Filter by category or difficulty
   - Click on recipe cards to view details

2. **View Recipe Details**
   - See full ingredients list
   - Follow step-by-step instructions
   - Watch cooking video (if available)
   - Leave ratings and reviews
   - Print recipe using print button
   - Share recipe on social media

3. **Explore Gallery**
   - View all culinary photos
   - Filter by category
   - Click images for lightbox view

4. **Watch Videos**
   - Browse cooking videos
   - Click to watch on YouTube/Vimeo

5. **Read Blog**
   - Browse blog posts
   - Read full articles
   - Share posts

## Project Structure

```
chef_portfolio/
├── chef_site/              # Project settings
├── portfolio/              # Chef profile and testimonials
├── recipes/               # Recipe management
├── gallery/               # Photos and videos
├── blog/                  # Blog posts
├── templates/             # HTML templates
│   ├── base.html
│   ├── portfolio/
│   ├── recipes/
│   ├── gallery/
│   └── blog/
├── static/                # Static files
│   ├── css/
│   │   └── style.css     # Main stylesheet with animations
│   ├── js/
│   │   └── main.js       # JavaScript functionality
│   └── images/
├── media/                 # User uploads
├── manage.py
├── requirements.txt
└── README.md
```

## Cooking Animations

The website features several cooking-themed animations:

### Background Animations
- **Steam**: Rising steam effects that fade in and out
- **Utensils**: Floating knife, spoon, and fork that gently move
- **Ingredients**: Falling tomato, carrot, and onion animations

### Interactive Animations
- **Chef Hat**: Bouncing logo in navigation
- **Recipe Cards**: Hover effects with image zoom
- **Stats Counter**: Animated number counting on scroll
- **Smooth Scrolling**: Elegant page transitions
- **Fade-in Effects**: Elements animate into view

## Customization

### Colors
Edit `static/css/style.css` to change the color scheme:
```css
:root {
    --primary-color: #FF6B6B;    /* Main red */
    --secondary-color: #FFA500;   /* Orange */
    --accent-color: #FFD93D;      /* Yellow */
}
```

### Animations
Adjust animation speeds and effects in `style.css`:
- Steam animation: `@keyframes steam-rise`
- Utensil floating: `@keyframes float-utensil`
- Ingredient falling: `@keyframes fall-ingredient`

### Content
All content is managed through the Django admin panel:
- Chef profile and bio
- Recipes with ingredients and instructions
- Gallery images and videos
- Blog posts and articles
- Testimonials and reviews

## Features Breakdown

### Recipe System
- **Categories**: Organize recipes by type
- **Difficulty Levels**: Easy, Medium, Hard
- **Time Tracking**: Prep time and cook time
- **Servings**: Adjustable serving sizes
- **Ingredients**: Line-by-line ingredient list
- **Instructions**: Step-by-step cooking directions
- **Images**: Featured recipe photos
- **Videos**: Optional cooking video links
- **Ratings**: User reviews and star ratings

### Gallery System
- **Image Upload**: High-quality photo uploads
- **Categories**: Filter images by category
- **Lightbox**: Click to view full-size images
- **Descriptions**: Add context to photos
- **Featured Images**: Highlight best work

### Video System
- **YouTube Integration**: Embed YouTube videos
- **Vimeo Support**: Also supports Vimeo
- **Thumbnails**: Custom video thumbnails
- **Duration**: Display video length
- **Descriptions**: Add video context

### Blog System
- **Rich Content**: Full article support
- **Featured Images**: Eye-catching visuals
- **Excerpts**: Preview text for listings
- **View Counter**: Track article popularity
- **Related Posts**: Show similar content
- **Share Buttons**: Social media sharing

## SEO & Performance

- Semantic HTML structure
- Optimized images
- Fast page load times
- Mobile-responsive design
- Clean URL structure
- Meta tags support

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## Future Enhancements

- User accounts and profiles
- Recipe collections/favorites
- Meal planning features
- Shopping list generator
- Nutritional information
- Recipe scaling calculator
- Email newsletter
- Advanced search filters
- Recipe import/export
- Multi-language support

## Support

For issues or questions:
- Email: chef@alessandro.com
- Check Django documentation: https://docs.djangoproject.com/

## License

This project is created for portfolio purposes.

---

**Made with ❤️ and 🍳 for passionate chefs**