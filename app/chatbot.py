from numpy import full
import streamlit as st
import openai
from config import GPT_MODEL
from chat_context_provider import query_message, fetch_topic_embedding

### BOT APP
def bot_streaming_function(prompt, topic_embeddings_df, GPT_MODEL, token_budget):
    """
    The bot_streaming_function function takes in a prompt, topic_embeddings_df, GPT-3 model name and token budget.
    It then queries the GPT-3 model with the given prompt and returns a response.
    The bot_streaming function is used to stream responses from the OpenAI API.

    :param prompt: Pass the initial user input to the bot
    :param topic_embeddings_df: Pass the topic embeddings dataframe to the bot_streaming_funtion function
    :param GPT_MODEL: Pass the gpt model to the bot_streaming_functions function
    :param token_budget: Limit the number of tokens that can be generated in a response
    :return: A generator object
    """

    full_response = ""
    message = query_message(prompt, topic_embeddings_df, GPT_MODEL, token_budget)
    messages = [
    {"role": "system", "content": "You answer questions about the business process management, large_language_models, Natural Language Processing,  Optical Character Recognition, Speech Recognition."},
    {"role": "user", "content": message},
    ]
    #messages.extend(message_content)
    response_generator = openai.ChatCompletion.create(model=GPT_MODEL, messages=messages, temperature = 0.4, stream = True)

    for response in response_generator:
            full_response += response.choices[0].delta.get("content", "")
            yield full_response

st.set_page_config(
    page_title="Wikipedia Bot",
    page_icon=":robot:"
)

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
openai.api_key = OPENAI_API_KEY

st.title('Wikipedia Knowledge Bot')
st.subheader("Ask questions about below topics:")
st.markdown("""
            * Business Process Management
            * Large Language Models
            * Natural Language Processing
            * Optical Character Recognition
            * Speech Recognition
            """)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

topic_embeddings_df = fetch_topic_embedding()

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What do you wnat to know up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        #full_response = ""
        stream_response = ""
        #messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
        for stream_response in bot_streaming_function(prompt, topic_embeddings_df, GPT_MODEL, 1000):
            message_placeholder.markdown(stream_response + "▌")
        # Simulate stream of response with milliseconds delay
        full_response = stream_response
    message_placeholder.markdown(full_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
