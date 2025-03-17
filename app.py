# Import necessary libraries for natural language processing, web development, and database management
import nltk
from nltk.stem import WordNetLemmatizer
import spacy
import sqlite3
from flask import Flask, request, render_template_string

# Initialize spaCy and load the English NLP model
nlp = spacy.load("en_core_web_sm")

# Download NLTK models for tokenizing and lemmatizing text
nltk.download('punkt')
nltk.download('wordnet')

# Function to process text using NLTK (tokenization and lemmatization)
def process_text(text):
    """
    Processes the given text by tokenizing and lemmatizing words to normalize them.
    
    Args:
        text (str): The text to be processed.
    
    Returns:
        list: List of processed words.
    """
    lemmatizer = WordNetLemmatizer()
    tokens = nltk.word_tokenize(text)
    # Apply lemmatization to reduce words to their base form
    tokens = [lemmatizer.lemmatize(token.lower()) for token in tokens]
    return tokens

# Function to process questions using spaCy for entity recognition
def process_question_with_spacy(question):
    """
    Processes the given question using spaCy to identify entities.
    
    Args:
        question (str): The user's question.
    
    Returns:
        list: List of entities found in the question.
    """
    doc = nlp(question)
    entities = []
    for ent in doc.ents:
        entities.append((ent.text, ent.label_))
    return entities

# Function to query product details from the database
def get_product_details(product_name):
    """
    Queries product details from the database based on the product name.
    
    Args:
        product_name (str): The name of the product.
    
    Returns:
        str: Product details or a message if the product is not found.
    """
    conn = sqlite3.connect('electronics_store.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT name, description, price, stock_quantity FROM products WHERE name LIKE ?", ('%' + product_name + '%',))
    product_info = cursor.fetchone()
    
    conn.close()
    
    if product_info:
        return f"Product Name: {product_info[0]}, Description: {product_info[1]}, Price: ${product_info[2]:.2f}, Stock Available: {product_info[3]}"
    else:
        return "Sorry, I couldn't find that product. Could you check the name or try another one?"

# Function to list all available products
def list_all_products():
    """
    Lists all available products from the database.
    
    Returns:
        str: List of product names.
    """
    conn = sqlite3.connect('electronics_store.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM products")
    products = cursor.fetchall()
    conn.close()
    return ", ".join([product[0] for product in products])

# Function to get employee details from the database
def get_employee_details(employee_name):
    """
    Queries employee details from the database based on the employee name.
    
    Args:
        employee_name (str): The name of the employee.
    
    Returns:
        str: Employee details or a message if the employee is not found.
    """
    conn = sqlite3.connect('electronics_store.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT name, position, email FROM employees WHERE name LIKE ?", ('%' + employee_name + '%',))
    employee_info = cursor.fetchone()
    
    conn.close()
    
    if employee_info:
        return f"Employee Name: {employee_info[0]}, Position: {employee_info[1]}, Email: {employee_info[2]}"
    else:
        return "Employee not found."

# Function to get order details from the database
def get_order_details(customer_name):
    """
    Queries order details from the database based on the customer name.
    
    Args:
        customer_name (str): The name of the customer.
    
    Returns:
        str: Order details or a message if the order is not found.
    """
    conn = sqlite3.connect('electronics_store.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT c.name, o.id, o.order_date, o.total FROM customers c JOIN orders o ON c.id = o.customer_id WHERE c.name LIKE ?", ('%' + customer_name + '%',))
    order_info = cursor.fetchall()
    
    conn.close()
    
    if order_info:
        response = ""
        for order in order_info:
            response += f"Customer Name: {order[0]}, Order ID: {order[1]}, Order Date: {order[2]}, Total: ${order[3]:.2f}\n"
        return response
    else:
        return "Order not found for that customer."

# Function to respond to user queries based on predefined rules and database queries
def respond_to_question(question):
    """
    Responds to a user query based on predefined rules and entities detected by spaCy.
    
    Args:
        question (str): The user's question.
    
    Returns:
        str: The corresponding response.
    """
    # Convert the question to lowercase for easier comparison
    question = question.lower()
    
    # Process the question with spaCy to identify entities
    entities = process_question_with_spacy(question)
    
    # Debugging: Print identified entities
    print("Entities:", entities)
    
    # Use entities to improve responses
    for entity, label in entities:
        if label == "ORG":
            return f"You mentioned '{entity}'. How can I assist you with this organization?"
        elif label == "GPE":
            return f"You mentioned '{entity}'. Are you asking about a location?"
        elif label == "PERSON":
            # Use the entity name to query employee details
            return get_employee_details(entity)
    
    # Check predefined conditions for keywords
    if "hours" in question or "opening hours" in question:
        return "Our business hours are Monday to Friday, 9am to 5pm. We're closed on weekends and holidays."
    
    elif "location" in question or "address" in question:
        return "We are located at 123 Business Street, Cityville. You can find us easily using GPS or public transportation."
    
    elif "price" in question or "cost" in question or "product" in question:
        # Extract product name from the question (last word as a basic example)
        product_name = question.split()[-1]
        return get_product_details(product_name)
    
    elif "products available" in question or "what products do you have available" in question:
        return f"We have the following products available: {list_all_products()}"
    
    elif "employee" in question or "employees" in question:
        # Extract employee name from the question (last word as a basic example)
        employee_name = question.split()[-1]
        return get_employee_details(employee_name)
    
    elif "order" in question or "orders" in question:
        # Extract customer name from the question (last word as a basic example)
        customer_name = question.split()[-1]
        return get_order_details(customer_name)
    
    elif "services" in question:
        return "We offer consulting, development, and support services. Let us know how we can assist you!"
    
    elif "contact" in question or "phone" in question or "email" in question:
        return "You can reach us by phone at 555-1234 or via email at info@example.com. We're happy to help!"
    
    elif "career" in question or "job" in question:
        return "We're always looking for talented individuals to join our team. Check our careers page for current openings."
    
    elif "faq" in question:
        return "Please visit our FAQs page for answers to frequently asked questions. If you can't find what you're looking for, feel free to ask us directly."
    
    # If none of the above conditions match, return a friendly generic message
    return "I'm sorry, I didn't quite understand that. Could you rephrase or give me more context? I'm here to help!"

# HTML template for chatbot interface (simple and clean design)
template = """
<!DOCTYPE html>
<html>
<head>
<title>Chatbot</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
<style>
body {
    background: #f0f0f0;
    font-family: Arial, sans-serif;
}
.container {
    margin-top: 50px;
}
.chatbox {
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
h1 {
    color: #00698f;
    text-align: center;
}
#chat-history {
    margin-top: 20px;
    background-color: #e9ecef;
    padding: 15px;
    border-radius: 10px;
    max-height: 300px;
    overflow-y: auto;
}
.chat-entry {
    margin-bottom: 10px;
}
.chat-entry strong {
    color: #00698f;
}
</style>
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">Chatbot</a>
</nav>

<div class="container">
  <div class="chatbox">
    <h1>Chatbot</h1>
    <p class="text-center text-muted">Hello! How can I assist you today?</p>
    
    <form action="/" method="post">
      <div class="mb-3">
        <input type="text" name="pregunta" class="form-control" placeholder="Ask me a question">
      </div>
      <button type="submit" class="btn btn-success w-100">Send</button>
    </form>

    {% if respuesta %}
    <div id="chat-history">
      {% for entry in chat_history %}
      <div class="chat-entry">
        <p><strong>You:</strong> {{ entry.question }}</p>
        <p><strong>Chatbot:</strong> {{ entry.response }}</p>
      </div>
      {% endfor %}
      <div class="chat-entry">
        <p><strong>You:</strong> {{ pregunta }}</p>
        <p><strong>Chatbot:</strong> {{ respuesta }}</p>
      </div>
    </div>
    {% endif %}
    
  </div>
</div>

<script src="https://kit.fontawesome.com/a076d05399.js" crossorigin="anonymous"></script>
</body>
</html>"""


# Create a Flask application instance
app = Flask(__name__)

# Define the main route for handling chatbot interactions
@app.route('/', methods=['GET', 'POST'])
def index():

    """
    Handles user interactions with the chatbot via GET and POST requests.
    
    Returns:
        str: Rendered HTML template with chatbot responses.
    """
    if request.method == 'POST':
        # Get the user's input from the form data
        question = request.form['pregunta']
        
        # Generate a response based on the user's input
        response = respond_to_question(question)
        
        # Render the template with the chatbot's response
        return render_template_string(template, respuesta=response)
    
    else:
        # Render the template without a response for GET requests
        return render_template_string(template)

# Run the application if executed directly (development mode enabled)
if __name__ == '__main__':
    app.run(debug=True)