import os
import json
import sys
from flask import render_template, request, flash, redirect, url_for, jsonify
from app import app
from .models import ContactForm
from .utils import save_to_json, save_order
from .products_data import products, get_product_by_id

# Adding the project directory to the sys.path for module access
sys.path.insert(0, '/Users/svetlanamelichova/Desktop/wooden-products-website')

# Route to render the home page


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    # Additional logic for POST requests can be added here
    return render_template('index.html')

# Route to handle the contact form submission


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm(request.form)
    if request.method == 'POST' and form.validate():
        data = form.data
        save_to_json(data)  # Saving the form data to a JSON file
        return redirect(url_for('contact.html'))
    return render_template('contact.html', form=form)

# Route to handle email sending and saving data to a JSON file


@app.route('/send_email', methods=['POST'])
def send_email():
    # Collecting form data
    data = {
        "name": request.form.get('name'),
        "phone": request.form.get('phone'),
        "email": request.form.get('email'),
        "inquiryType": request.form.get('inquiryType'),
        "county": request.form.get('county'),
        "message": request.form.get('message')
    }
    # Saving data and returning appropriate JSON response
    if save_to_json(data):
        return jsonify({"message": "Email Sent and Data Saved!", "data": data})
    else:
        return jsonify({"message": "Failed to Save Data", "data": data})

# Routes for rendering FAQ and About pages


@app.route("/FAQ")
def faq():
    return render_template('FAQ.html')


@app.route("/about")
def about():
    return render_template('about.html', products=products)

# Route to render the products page


@app.route("/products")
def products_page():
    return render_template('products.html', products=products)

# Route to render a specific product detail page


@app.route('/product/<int:product_id>')
def product_detail(product_id):
    # Finding a specific product by ID
    product = get_product_by_id(product_id)
    if product:
        return render_template('product_details.html', product=product)
    else:
        flash('Product not found!', 'error')
        return redirect(url_for('products_page'))

# Route to handle the order placement


@app.route('/place_order', methods=['POST'])
def place_order():
    # Collecting order data from form
    order_data = {
        "product_id": request.form.get('product_id'),
        "size": request.form.get('size'),
        "material": request.form.get('material'),
        "roof": request.form.get('roof'),
        "color": request.form.get('color')
    }
    # Saving the order and returning JSON response
    if save_order(order_data):
        return jsonify({"success": True, "message": "Order placed successfully!", "order_data": order_data})
    else:
        return jsonify({"success": False, "message": "There was an error placing the order."})

# Route for submitting product reviews


@app.route('/submit_review', methods=['POST'])
def submit_review():
    try:
        # Collecting review data
        review_data = {
            "product_id": request.form.get('product_id'),
            "review": request.form.get('review'),
            "rating": request.form.get('rating')
        }
        # Path to the file storing reviews
        reviews_file = 'reviews.json'
        # Check if the file exists and is not empty
        if not os.path.exists(reviews_file) or os.path.getsize(reviews_file) == 0:
            reviews = []
        else:
            with open(reviews_file, 'r') as file:
                reviews = json.load(file)
        # Adding new review and saving to file
        reviews.append(review_data)
        with open(reviews_file, 'w') as file:
            json.dump(reviews, file, indent=4)
        return jsonify({"message": "Review submitted successfully", "success": True})
    except json.JSONDecodeError:
        # Handling empty file scenario
        return jsonify({"message": "JSON decode error, possibly empty file", "success": False})
    except Exception as e:
        # General error handling
        return jsonify({"message": "Failed to submit review", "success": False, "error": str(e)})
