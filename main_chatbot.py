import streamlit as st
import streamlit_chat
from streamlit_chat import message as st_message
from transformers import pipeline, Conversation

if "history" not in st.session_state:
    st.session_state.history = []
st.title("ChatBot")
def main():
    chatbot = pipeline(model="facebook/blenderbot-400M-distill")


    user_input = st.text_input('User:', "")

    if user_input.lower() == "bye":
        print('Chatbot : Goodbye!')

    else:
        conversation = Conversation()
        conversation.add_user_input(user_input)
        conversation = chatbot(conversation)

        chatbot_response = conversation.generated_responses[-1]

    st.session_state.history.append({"message": user_input, "is_user": True})
    st.session_state.history.append({"message": chatbot_response, "is_user": False})

if __name__ == "__main__":
    main()

for i, chat in enumerate(st.session_state.history):
    st_message(**chat, key=str(i))
