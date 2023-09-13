import logging
import streamlit as st
import openai
import pandas as pd
import ast  # for converting embeddings saved as strings back to arrays
#from database import get_redis_connection, get_redis_results
from config import GPT_MODEL, OPENAI_API_KEY
from chat_context_provider import query_message

### SEARCH APP

st.set_page_config(
    page_title="Wikipedia Search",
    page_icon=":robot:"
)

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

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    topic_embeddings_df = pd.read_csv('data/embedding/topic_embedding.csv')
    # convert embeddings from CSV str type back to list type
    topic_embeddings_df['embedding'] = topic_embeddings_df['embedding'].apply(ast.literal_eval)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
        message = query_message(prompt, topic_embeddings_df, GPT_MODEL, 1000)
        message_content = [
        {"role": "system", "content": "You answer questions about the business process management, large_language_models, Natural Language Processing,  Optical Character Recognition, Speech Recognition."},
        {"role": "user", "content": message},
        ]
        messages.extend(message_content)
        response_generator = openai.ChatCompletion.create(model=GPT_MODEL, messages=messages, temperature = 0.4, stream = True)
        # Simulate stream of response with milliseconds delay
        for response in response_generator:
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})