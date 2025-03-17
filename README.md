# Chatbot Project
================

A conversational AI designed to assist with common business inquiries.

## Description
------------

This chatbot uses Python with NLTK and spaCy for natural language processing. It is designed to handle common user queries about business hours, location, services, pricing, and more. The chatbot is deployed using Flask as a web interface.

## Technologies Used
--------------------

- Python
- NLTK
- spaCy
- Flask (for web interface)

## Features
-----------

- **Business Hours**: Provides information about the company's opening hours.
- **Location**: Shares the company's address and directions.
- **Pricing**: Responds to questions about product or service costs.
- **Services**: Lists available services offered by the company.
- **Products**: Offers details about the company's products.
- **Contact Information**: Provides phone numbers and email addresses for customer support.
- **Careers**: Shares information about job opportunities.
- **Entity Recognition with spaCy**: Identifies entities in user queries to improve responses.

## Configuration
--------------

### Setting Up the Environment

To configure the environment, follow these steps:

1. **Create a new conda environment**:



```conda create --name chatbot_project python=3.9```


2. **Activate the environment**:

```conda activate chatbot_project```


3. **Install required packages**:

```conda install nltk spacy flask```


4. **Download NLTK and spaCy models**:

```python -c "import nltk; nltk.download('punkt'); nltk.download('wordnet')"```
```python -m spacy download en_core_web_sm```


## How to Run
--------------

1. Clone the repository.

```git clone https://github.com/jopriera/Artificial_Intelligence_Portfolio/.git```


2. Navigate to the project directory:

```cd chatbot_project```



3. Activate the environment:

```conda activate chatbot_project```



4. Run the chatbot:

```python app.py```



5. Open your browser and go to:

```http://127.0.0.1:5000/```


## Example Use Cases
--------------------

Here are some examples of questions you can ask the chatbot:

1. **Business Hours**:
- "What are your business hours?"
- "When do you open?"

2. **Location**:
- "Where are you located?"
- "What is your address?"

3. **Pricing**:
- "How much does it cost?"
- "What is the price of your services?"

4. **Services**:
- "What services do you offer?"
- "Can you tell me about your consulting services?"

5. **Products**:
- "What products do you sell?"
- "Do you have any new arrivals?"

6. **Contact Information**:
- "How can I contact you?"
- "What is your phone number?"

7. **Careers**:
- "Are there any job openings?"
- "How can I apply for a job?"

8. **FAQs**:
- "Where can I find FAQs?"
- "Do you have a help page?"

---

## Next Steps
--------------

1. **Improve Entity Recognition**: Enhance spaCy integration to handle more complex queries.
2. **Database Integration**: Store data in a database (e.g., SQLite or MongoDB) for dynamic responses.
3. **Web Interface Design**: Improve the web interface using CSS or frameworks like Bootstrap.
4. **Logging and Error Handling**: Add logging and error handling for better debugging and monitoring.

---

## License
----------

This project is licensed under the MIT License.