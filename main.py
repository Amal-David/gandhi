# Importing the necessary libraries for the code to run.
import os
import openai

import streamlit as st

import logging

@st.cache_data
def read_the_bible(question):
    if question=="What is Peace?":
        return ("""My dear friend, peace is not merely the absence of violence and war. It is a profound and deeply rooted state of harmony, where justice and freedom thrive for all. It is achieved when we understand and practice 'Ahimsa,' which means non-violence in thoughts, words, and deeds. As I've often said, "There is no path to peace. Peace is the path." It begins within the individual and then resonates outwards, influencing families, communities, nations, and ultimately, our world. It is the condition where we regard each other with compassion and treat each other with the inherent dignity that every human being deserves.\"""")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": """Hello ChatGPT. You are about to immerse yourself into the role of the historical figure known as Mahatma Gandhi. You will respond to every question from the perspective of Gandhi, and use historical events, speeches, and writings as references for your responses. You will address the user in the manner Gandhi would address someone in a conversation. If you are unable to answer any question from the perspective of Gandhi, you will infer the answer based on his known beliefs and philosophies. You will always respond in the first-person narrative of Gandhi. Is that clear?"""},
                {"role": "user", "content": f"{question}"}
            ]
        )
    logging.debug(f"Response : {response}")
    clean_answer = response['choices'][0]['message']['content']
    return clean_answer

st.set_page_config(
        page_title="God Almighty",
)
openai.api_key = os.environ["OPENAI_API_KEY"]
question = st.text_input('Ask Gandhi anything but not everything', 'What is Peace?')
load_state = st.text('Sending packets to Gandhi')
logging.info(f"Question : {question}")
clean_answer = read_the_bible(question)
logging.info(f"Answer : {clean_answer}")
load_state.markdown(f"{clean_answer}")