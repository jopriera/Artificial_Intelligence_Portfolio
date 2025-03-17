# Import necessary libraries for natural language processing and web development
import nltk
from nltk.stem import WordNetLemmatizer
import spacy
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

# Function to respond to user queries based on predefined rules

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
    print("Entities:", entities)  # Debugging: Print identified entities
    
    # Use entities to improve responses
    for entity, label in entities:
        if label == "ORG":  # Organization detected
            return f"You mentioned '{entity}'. How can I help you with this organization?"
        elif label == "GPE":  # Geographic Political Entity detected
            return f"You mentioned '{entity}'. Are you asking about a location?"
        elif label == "PERSON":  # Person detected
            return f"You mentioned '{entity}'. Are you asking about someone specific?"
    
    # Check predefined conditions for keywords
    if "hours" in question or "opening hours" in question:
        return "Our business hours are Monday to Friday, 9am to 5pm. We're closed on weekends and holidays."
    elif "location" in question or "address" in question:
        return "We are located at 123 Business Street, Cityville. You can find us easily using GPS or public transportation."
    elif "price" in question or "cost" in question:
        return "Prices vary depending on the product. Please specify a product or service for more detailed pricing information."
    elif "services" in question:
        return "We offer a variety of services including consulting, development, and support. Let us know how we can assist you."
    elif "products" in question:
        return "We have a wide range of products available. Please visit our website or contact us for more details."
    elif "contact" in question or "phone" in question or "email" in question:
        return "You can reach us by phone at 555-1234 or via email at info@example.com. We're always happy to help."
    elif "career" in question or "job" in question:
        return "We're always looking for talented individuals to join our team. Check our careers page for current openings."
    elif "faq" in question:
        return "Please visit our FAQs page for answers to frequently asked questions. If you can't find what you're looking for, feel free to ask us directly."
    
    # If none of the above conditions match, return a generic message
    return "I'm sorry, I didn't understand your question. Could you please rephrase or provide more details?"

# HTML template for chatbot interface (simple and clean design)
template = """
<!DOCTYPE html>
<html>
<head>
    <title>Chatbot</title>
</head>
<body>
    <h1>Chatbot</h1>
    <form action="/" method="post"> <!-- Changed from /pregunta to / -->
        <input type="text" name="pregunta" placeholder="Ask me a question">
        <input type="submit" value="Send">
    </form>
    {% if respuesta %}
        <p>Response: {{ respuesta }}</p>
    {% endif %}
</body>
</html>
"""

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

