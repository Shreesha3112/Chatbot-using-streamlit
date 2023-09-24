# Wikipedia Chatbot

This is an Open AI based chatbot made with Streamlit. Follow the instructions below to get set up.

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/).

2. Clone this repository.

3. Navigate into the project directory:

   ```bash
   $ cd Wikipedia-Chatbot
   ```

4. Create a new virtual environment:

   ```bash
   $ python -m venv venv
   ```
   Activate virtual environment
   
   For linux/ Mac users

   ```bash
   $ . venv/bin/activate
   ```
   For windows users

   ```bash
   $ . venv\Scripts\Activate
   ```

5. Install the requirements:

   ```bash
   $ pip install -r requirements.txt
   ```

6. Make a copy of the example secrets variables file:

   ```bash
   $ cp .streamlit/secrets.example.toml .streamlit/secrets.toml
   ```

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `secrets.toml` file.

8. Run the app:

   ```bash
   $ streamlit run app/chatbot.py
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

## Chatbot uses Search-Ask approach using embedding search 

#### Why search is better than fine-tuning

GPT can learn knowledge in two ways:

- Via model weights (i.e., fine-tune the model on a training set)
- Via model inputs (i.e., insert the knowledge into an input message)

Although fine-tuning can feel like the more natural option—training on data is how GPT learned all of its other knowledge, after all—we generally do not recommend it as a way to teach the model knowledge. Fine-tuning is better suited to teaching specialized tasks or styles, and is less reliable for factual recall.

As an analogy, model weights are like long-term memory. When you fine-tune a model, it's like studying for an exam a week away. When the exam arrives, the model may forget details, or misremember facts it never read.

In contrast, message inputs are like short-term memory. When you insert knowledge into a message, it's like taking an exam with open notes. With notes in hand, the model is more likely to arrive at correct answers.

## Scope for Improvements

Q&A retrieval performance may also be improved with techniques like [HyDE](https://arxiv.org/abs/2212.10496), in which questions are first transformed into hypothetical answers before being embedded. Similarly, GPT can also potentially improve search results by automatically transforming questions into sets of keywords or search terms.

## Test cases

1. Counting question 
   
3. Comparision quetion - 

4. Subjective quetion

5. False assumption quetion

6. 'instruction injection' question

7. Misspelled question

8. Out of scope quetion

9. open-ended question

