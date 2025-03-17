# Initialize natural language processing with NLTK
import nltk
from nltk.stem import WordNetLemmatizer
from flask import Flask, request, render_template_string

# Download necessary NLTK models for tokenizing and lemmatizing text
nltk.download('punkt')
nltk.download('wordnet')

# Define a function to process text, tokenizing and lemmatizing words
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

# Implement a function to respond to user queries
def respond_to_question(question):
    """
    Responds to a user query based on a set of predefined responses.
    
    Args:
        question (str): The user's question.
    
    Returns:
        str: The corresponding response.
    """
    # Convert the question to lowercase for easier comparison
    question = question.lower()
    
    # Check if the question is about business hours
    if "hours" in question or "opening hours" in question:
        return "Our business hours are Monday to Friday, 9am to 5pm. We're closed on weekends and holidays."
    
    # Check if the question is about location
    elif "location" in question or "address" in question:
        return "We are located at 123 Business Street, Cityville. You can find us easily using GPS or public transportation."
    
    # Check if the question is about prices
    elif "price" in question or "cost" in question:
        return "Prices vary depending on the product. Please specify a product or service for more detailed pricing information."
    
    # Check if the question is about services
    elif "services" in question:
        return "We offer a variety of services including consulting, development, and support. Let us know how we can assist you."
    
    # Check if the question is about products
    elif "products" in question:
        return "We have a wide range of products available. Please visit our website or contact us for more details."
    
    # Check if the question is about contact information
    elif "contact" in question or "phone" in question or "email" in question:
        return "You can reach us by phone at 555-1234 or via email at info@example.com. We're always happy to help."
    
    # Check if the question is about careers or jobs
    elif "career" in question or "job" in question:
        return "We're always looking for talented individuals to join our team. Check our careers page for current openings."
    
    # Check if the question is about FAQs
    elif "faq" in question:
        return "Please visit our FAQs page for answers to frequently asked questions. If you can't find what you're looking for, feel free to ask us directly."
    
    # If none of the above conditions match, return a generic message
    else:
        return "I'm sorry, I didn't understand your question. Could you please rephrase or provide more details?"

# Define a basic HTML template for our chatbot interface
template = """
<!DOCTYPE html>
<html>
<head>
    <title>Chatbot</title>
</head>
<body>
    <h1>Chatbot</h1>
    <form action="/" method="post"> <!-- Cambiado de /pregunta a / -->
        <input type="text" name="pregunta" placeholder="Ask me a question">
        <input type="submit" value="Send">
    </form>
    {% if respuesta %}
        <p>Response: {{ respuesta }}</p>
    {% endif %}
</body>
</html>
"""

# Create a new Flask application instance
app = Flask(__name__)

# Define the main route for our application
@app.route('/', methods=['GET', 'POST'])
def index():
    # If the user submits a form (POST request), process the question
    if request.method == 'POST':
        # Get the user's question from the form data
        question = request.form['pregunta']
        # Process the question and get a response
        response = respond_to_question(question)
        # Render the template with the response
        return render_template_string(template, respuesta=response)
    else:
        # For GET requests, just render the template without a response
        return render_template_string(template)

# Run the application if this script is executed directly
if __name__ == '__main__':
    # Enable debug mode for easier development
    app.run(debug=True)

