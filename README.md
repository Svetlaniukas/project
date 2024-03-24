# Wooden Project Website

## Overview

The Wooden Project Website is a Flask-based application designed to provide users with an interactive platform for browsing and purchasing wooden products. The website offers various features, including displaying product details, customizing product options, placing orders, and receiving order confirmations.

## Features

### Displaying the Home Page

When a visitor accesses the home page, either through the root URL `/` or `/home`, the application renders the `index.html` template via `routes.py`. This page serves as the welcoming point and gives a brief overview of what the store offers.

### Navigating to the Products Page

Clicking on the "Products" link triggers a route defined in `routes.py` that leads to the `/products` page. Here, visitors can view all available products. This page is populated by fetching product data from `products_data.py` and displaying it on `products.html`.

### Viewing Individual Product Details

Each product on the products page has a "See More" button. Clicking on this button directs the visitor to a detailed view of that particular product. This is handled by a specific route in `routes.py` that uses the product's ID to retrieve its details from `products_data.py` and display them on `product_detail.html`.

### Selecting Product Options and Calculating Costs

On the product detail page, visitors can customize their product by selecting different options like size, material, roof type, and color. As these options are selected, a JavaScript function in `custom.js` dynamically updates the total cost of the product. This script calculates the price by adding the base price of the product to the additional costs of the selected options.

### Placing an Order

Once the visitor is satisfied with their selection, they can place an order by submitting the form. This action sends a POST request to the `/place_order` route in `routes.py`. The submitted data, including the selected options and product ID, is processed, and the order details are saved in an `orders.json` file by the `save_order` function in `utils.py`.

### Order Confirmation

After successfully placing the order, the user is redirected to the home page with a confirmation message (a flash message) indicating the successful order placement. This message is generated and displayed by a function in `routes.py`.

## Project Structure

The project is structured as follows:

- **Root Directory: `/wooden-project-website`**
  - **Virtual Environment: `/venv`**
  - **Application Directory: `/app`**
    - **`__init__.py`**: Initializes the Flask application.
    - **Static Files Directory: `/static`**: Stores CSS, JavaScript, and image files.
    - **Templates Directory: `/templates`**: Contains Jinja2 templates.
    - **Routes File: `routes.py`**: Defines routing logic.
    - **Models File: `models.py`**: Contains database schema definitions.
    - **Utility Functions: `utils.py`**: A compilation of helper functions and utilities that support various operations within the application.
  - **Main Application File: `run.py`**: Serves as the entry point for running the Flask application.
  - **Dependencies List: `requirements.txt`**: Contains the list of project dependencies.

## Event Sequence in the Mini Wooden Products Store

### Displaying the Home

- **File:** `routes.py`
- **Description:** Accessing the home page (`/` or `/home`) renders the `index.html` template using Flask.

### Viewing the Products Page

- **File:** `routes.py`
- **Description:** Clicking on the "Products" link leads to the `/products` page, displaying a list of products from `products_data.py` on `products.html`.

### Detailed Product View

- **Files:** `routes.py`, `products_data.py`
- **Description:** Selecting a specific product redirects the user to `/product/<product_id>`. Flask uses `product_id` to fetch information from `products_data.py` and renders `product_detail.html`.

### Selecting Product Options

- **File:** `product_detail.html`
- **Description:** On the product detail page, users can select various options (size, material, etc.) from dropdown lists.

### Calculating Cost

- **Files:** `product_detail.html`, `custom.js`
- **Description:** After selecting options, `custom.js` automatically calculates the total cost using the base price and additional prices of options.

### Orders

- **Files:** `routes.py`, `utils.py`
- **Description:** Upon clicking "Place Order", form data is sent to `/place_order`. Flask processes the POST request, and the `save_order` function in `utils.py` saves the order details in `orders.json`.

### Order Confirmation Notification

- **File:** `routes.py`
- **Description:** After successful order placement, the user receives a notification (flash message) and is redirected to the home page.

## Function Descriptions

### save_to_json(data, filename='form_data.json')

This function is a comprehensive utility for serializing and storing data in JSON format. It accepts two parameters: the data to be saved and an optional filename, which defaults to 'form_data.json'. The function opens the specified file in write mode and writes the data into it in JSON format, ensuring the output is well-formatted and easily readable. If successful, it logs an informational message and returns True as a confirmation. In the event of exceptions, such as file access issues, it logs a detailed error message and returns False. This method is essential for maintaining data integrity and simplifies debugging.

### save_order(order_data)

The `save_order` function handles the storage of order data in a JSON file, ensuring thread safety with Python's file handling capabilities. It starts by checking if 'orders.json' exists and creates it with an empty list if not. The function then opens this file and appends new `order_data` to the existing list of orders. It ensures that the updated list is written back to the file correctly. The function returns True if the process is successful or prints an error and returns False in case of an exception. This function is vital for organizing and storing order data efficiently.

### convert_from_record_to_int(record)

This function is designed to convert a specified record into an integer. It primarily operates by extracting the first element of the given record, and then converting the first element of this extracted data into an integer. This function is particularly useful for processing data where type conversion from a record format to an integer is necessary.
# ucd-project
# ucd-project
# wooden-products-website
# flask_ucd
# flask_ucd
# project
# project
