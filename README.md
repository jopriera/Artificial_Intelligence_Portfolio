# Chatbot Project
================

A conversational AI designed to assist with common business inquiries.

## Description
------------

This chatbot uses Python with NLTK and spaCy for natural language processing. It is designed to handle common user queries about business hours, location, services, pricing, and more. The chatbot is deployed using Flask as a web interface.

While some features are fully functional, others (like querying products and orders) are still under development.

## Technologies Used
--------------------

- Python
- NLTK
- spaCy
- Flask (for web interface)
- SQLite (for database integration)
- CSS (for web interface styling)

## Features
-----------

- **Business Hours**: Provides information about the company's opening hours. *(Functional)*
- **Location**: Shares the company's address and directions. *(Currently not working as expected)*
- **Pricing**: Responds to questions about product or service costs. *(Functional for specific queries)*
- **Services**: Lists available services offered by the company. *(Functional)*
- **Products**: Offers details about the company's products. *(Partially functional; listing all products is under review)*
- **Contact Information**: Provides phone numbers and email addresses for customer support. *(Functional)*
- **Careers**: Shares information about job opportunities. *(Functional)*
- **Entity Recognition with spaCy**: Identifies entities in user queries to improve responses. *(Functional)*

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

## Known Issues and Limitations
--------------------

1. **Product Listing**:
   - Currently, the chatbot does not correctly respond to the question "What products do you have available?" despite several attempts to resolve this issue.
   - Solutions attempted include modifying the query handling logic and ensuring database connections are correct.
   - If you have suggestions or would like to contribute a solution, please feel free to collaborate.

2. **Order Queries**:
   - The chatbot does not correctly respond to questions about orders, such as "What orders does John Doe have?".
   - Further refinement is needed to handle these queries effectively.

---

## Next Steps
--------------

1. **Fix Known Issues**: Address current bugs related to product listing and order queries.
2. **Improve Entity Recognition**: Enhance spaCy integration to handle more complex queries.
3. **Web Interface Design**: Improve the web interface using CSS or frameworks like Bootstrap.
4. **Logging and Error Handling**: Add logging and error handling for better debugging and monitoring.

---

## Conclusion
----------

This project demonstrates a basic conversational AI chatbot capable of handling common business inquiries. While some features are fully functional, others require further development. The chatbot serves as a foundation for more advanced NLP applications and can be expanded upon in the future.

---

## License
----------

This project is licensed under the MIT License.
```

---