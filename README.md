# Sagility-Generative-AI-assessment - Wikipedia Chatbot

## Setup


This is an Open AI based chatbot made with Streamlit. Follow the instructions below to get set up.

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/).

2. Clone this repository.

3. Navigate into the project directory:

   ```bash
   $ cd Sagility-Generative-AI-assessment
   ```

4. Create a new virtual environment:

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

5. Install the requirements:

   ```bash
   $ pip install -r requirements.txt
   ```

6. Make a copy of the example environment variables file:

   ```bash
   $ cp .env.example .env
   ```

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file.

8. Run the app:

   ```bash
   $ streamlit run chatbot.py
   ```

You should now be able to access the app at [http://localhost:8501](http://localhost:8501)!

## Wikipedia topics selected

1. [Business process management](https://en.wikipedia.org/wiki/Business_process_management)
2. [Large language model](https://en.wikipedia.org/wiki/Large_language_model)
3. [Natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing)
4. [Speech recognition](https://en.wikipedia.org/wiki/Speech_recognition)
5. [Optical character recognition](https://en.wikipedia.org/wiki/Optical_character_recognition)

## Objectives
1. Build an information retrieval system (Q&A bot) that can interface with your data (the 5 text files)
2. Q&A Bot should accurately respond to queries related to the contents of these files
3. Q&A bot must be built using a generative AI service such as OpenAI
4. Q&A bot should only respond to queries which are within the scope of your source documents
5. Build a simple web interface for this Q&A bot.

### 2. Q&A Bot should accurately respond to queries related to the contents of these files
Solution: Use fine tuning /
