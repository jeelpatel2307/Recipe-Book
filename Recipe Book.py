# app.py

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data for recipes
recipes = [
    {'id': 1, 'title': 'Pasta Carbonara', 'ingredients': 'Spaghetti, Guanciale, Eggs, Parmesan Cheese'},
    {'id': 2, 'title': 'Chicken Alfredo', 'ingredients': 'Fettuccine, Chicken, Alfredo Sauce'},
    {'id': 3, 'title': 'Chocolate Chip Cookies', 'ingredients': 'Flour, Butter, Sugar, Chocolate Chips'},
]

@app.route('/')
def index():
    return render_template('index.html', recipes=recipes)

@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    title = request.form.get('title')
    ingredients = request.form.get('ingredients')

    if title and ingredients:
        new_recipe = {'id': len(recipes) + 1, 'title': title, 'ingredients': ingredients}
        recipes.append(new_recipe)

    return redirect(url_for('index'))

@app.route('/delete_recipe/<int:recipe_id>')
def delete_recipe(recipe_id):
    global recipes
    recipes = [recipe for recipe in recipes if recipe['id'] != recipe_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)





<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recipe Book</title>
</head>
<body>

    <h1>Recipe Book</h1>

    <ul>
        {% for recipe in recipes %}
            <li>
                {{ recipe.title }} - {{ recipe.ingredients }}
                <a href="{{ url_for('delete_recipe', recipe_id=recipe.id) }}">Delete</a>
            </li>
        {% endfor %}
    </ul>

    <h2>Add New Recipe</h2>
    <form action="/add_recipe" method="post">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required>
        <br>
        <label for="ingredients">Ingredients:</label>
        <textarea id="ingredients" name="ingredients" required></textarea>
        <br>
        <input type="submit" value="Add Recipe">
    </form>

</body>
</html>
