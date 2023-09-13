# Sagility-Generative-AI-assessment - Wikipedia Chatbot

## Setup

1. Clone this repository.
2. Navigate into the project directory:
<$ cd openai-quickstart-python>
3. Create a new virtual environment:
<$ python -m venv venv
$ . venv/bin/activate>
4. Install the requirements:
$ pip install -r requirements.txt
5.Make a copy of the example environment variables file:
$ cp .env.example .env
6. Add your API key to the newly created .env file.
7. Run the app:
$ streamlit run chatbot.py


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
