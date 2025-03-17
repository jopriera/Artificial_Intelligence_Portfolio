# Initialize natural language processing with NLTK
import nltk
from nltk.stem import WordNetLemmatizer

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
    if "hours" in question.lower():
        # If the question includes the word "hours", respond with business hours
        return "Our business hours are Monday to Friday, 9am to 5pm."
    else:
        # If the question is not recognized, return a generic message
        return "I'm sorry, I don't understand your question."

# Example usage
if __name__ == "__main__":
    # Prompt the user to enter a question
    user_question = input("Ask me a question: ")
    # Get the corresponding response
    response = respond_to_question(user_question)
    # Display the response to the user
    print(response)
