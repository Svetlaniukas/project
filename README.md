# Wooden Project Website

Displaying the Home Page: When a visitor accesses the home page, either through the root URL / or /home, my application, via routes.py, renders the index.html template. This page serves as the welcoming point and gives a brief overview of what the store offers.
Navigating to the Products Page: Clicking on the "Products" link triggers a route defined in routes.py that leads to the /products page. Here, visitors can view all the available products. This page is populated by fetching product data from products_data.py and displaying it on products.html.
Viewing Individual Product Details: Each product on the products page has a "See More" button. Clicking on this button directs the visitor to a detailed view of that particular product. This is handled by a specific route in routes.py that uses the product's ID to retrieve its details from products_data.py and display them on product_detail.html.
Selecting Product Options and Calculating Costs: On the product detail page, visitors can customize their product by selecting different options like size, material, roof type, and color. As these options are selected, a JavaScript function in custom.js dynamically updates the total cost of the product. This script calculates the price by adding the base price of the product to the additional costs of the selected options.
Placing an Order: Once the visitor is satisfied with their selection, they can place an order by submitting the form. This action sends a POST request to the /place_order route in routes.py. The submitted data, including the selected options and product ID, is processed, and the order details are saved in a orders.json file by the save_order function in utils.py.
Order Confirmation: After successfully placing the order, the user is redirected to the home page with a confirmation message (a flash message) indicating the successful order placement. This message is generated and displayed by a function in routes.py.
Throughout the user's journey in my store, from browsing products to placing an order, each interaction is carefully handled by specific parts of the application. The combination of Flask routes, HTML templates, JavaScript functions, and utility scripts ensures a seamless and interactive shopping experience.
## Project Structure

The project is structured as follows:

### Root Directory: `/wooden-project-website`

The primary directory housing the Flask application and various configuration files.

#### Virtual Environment: `/venv`

A dedicated virtual environment for isolating the project's dependencies, ensuring a conflict-free setup.

#### Application Directory: `/app`

The heart of the Flask application, containing all the core components.

- **`__init__.py`**:  
  Initializes the Flask application, setting up necessary configurations and initializing various components like databases, blueprints, etc.

- **Static Files Directory: `/static`**  
  Stores static resources such as CSS files, JavaScript scripts, and images. These files contribute to the styling and interactive features of the web application.

- **Templates Directory: `/templates`**  
  Contains Jinja2 templates, which define the HTML structure for the web pages. This directory helps in rendering dynamic content.

- **Routes File: `routes.py`**  
  Defines the routing logic of the web application, mapping URLs to their respective view functions.

- **Models File: `models.py`**  
  Contains the database schema definitions, representing the data models used within the application.

- **Utility Functions: `utils.py`**  
  A compilation of helper functions and utilities that support various operations within the application.

#### Main Application File: `run.py`

Serves as the entry point for running the Flask application. It boots up the web server, making the application accessible.

#### Dependencies List: `requirements.txt`

# Event Sequence in the Mini Wooden Products Store

### Displaying the Home Page
- **File:** `routes.py`
- **Description:** Accessing the home page (`/` or `/home`) renders the `index.html` using Flask.

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

### Placing an Order
- **Files:** `routes.py`, `utils.py`
- **Description:** Upon clicking "Place Order", form data is sent to `/place_order`. Flask processes the POST request, and the `save_order` function in `utils.py` saves the order details in `orders.json`.

### Order Confirmation Notification
- **File:** `routes.py`
- **Description:** After successful order placement, the user receives a notification (flash message) and is redirected to the home page.

Key Features and Functionality

Displaying the Home Page
Functionality: Renders the homepage using Flask.
Path: / or /home.
File: routes.py.
Template: index.html.
Viewing the Products Page
Functionality: Shows a list of products.
Path: /products.
File: routes.py.
Template: products.html.
Data Source: products_data.py.
Detailed Product View
Functionality: Displays detailed information for a selected product.
Path: /product/<product_id>.
Files: routes.py, products_data.py.
Template: product_detail.html.
Selecting Product Options
Functionality: Allows users to customize products with different options.
Template: product_detail.html.
Options: Size, material, roof type, color.
Calculating Cost
Functionality: Dynamically calculates total cost based on selected options.
Files: product_detail.html, custom.js.
Placing an Order
Functionality: Processes order placement and saves details.
Path: /place_order.
Method: POST.
Files: routes.py, utils.py.
Data Storage: orders.json.
Order Confirmation Notification
Functionality: Provides confirmation to the user upon successful order placement.
File: routes.py.
Notification: Flash message.
Function Processing Overview

Function index in routes.py
Request Types: Handles both GET and POST requests.
Data Validation: Employs WTForms.
POST Method Processing: Processes validated data and saves it to a JSON file.
Rendering: Displays an HTML template (e.g., contact.html).
Function send_email in routes.py
Path: /send_email.
Request Type: Only POST.
Data Extraction: Directly from request.form.
Data Handling: Prints to console, with potential for future email integration.
Response: JSON response.
Comparative Analysis of index and send_email
Form Data Handling:
index: Utilizes WTForms for validation.
send_email: Direct data extraction, no validation.
Use Cases:
index: Ideal for comprehensive form handling.
send_email: Suited for direct data retrieval.
Development and Testing:
send_email: Beneficial for initial development stages.
JSON Response with jsonify
Usage: Converts data into JSON format for client-side processing.
Functionality: Essential for REST APIs in Flask applications.
Conclusion

Both index and send_email functions serve different purposes within the application, catering to distinct needs in data handling and user interaction. While index offers a complete solution with validation and response rendering, send_email provides a more streamlined approach for backend data processing.

# Function Descriptions

save_to_json(data, filename='form_data.json')

This function is a comprehensive utility for serializing and storing data in JSON format. It accepts two parameters: the data to be saved and an optional filename, which defaults to 'form_data.json'. The function opens the specified file in write mode and writes the data into it in JSON format, ensuring the output is well-formatted and easily readable. If successful, it logs an informational message and returns True as a confirmation. In the event of exceptions, such as file access issues, it logs a detailed error message and returns False. This method is essential for maintaining data integrity and simplifies debugging.

save_order(order_data)

The save_order function handles the storage of order data in a JSON file, ensuring thread safety with Python's file handling capabilities. It starts by checking if 'orders.json' exists and creates it with an empty list if not. The function then opens this file and appends new order_data to the existing list of orders. It ensures that the updated list is written back to the file correctly. The function returns True if the process is successful or prints an error and returns False in case of an exception. This function is vital for organizing and storing order data efficiently.

convert_from_record_to_int(record)

This function is designed to convert a specified record into an integer. It primarily operates by extracting the first element of the given record, and then converting the first element of this extracted data into an integer. This function is particularly useful for processing data where type conversion from a record format to an integer is necessary.# ucd-project
