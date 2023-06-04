import streamlit as st
from streamlit_chat import message as st_message
from middleware import *
    

# All calls (to other functions) from this function
def main_bot():
    main()
    st.title("Go ham, the bot is all yours now.")
    st.text_input(label="Enter your message here: ", key="bot_chat", placeholder="Type your message here...")
    history = [
        {
            "message": "Yo bde whats good",
            "is_user": False
        },
        {
            "message": "im good yo",
            "is_user": True
        },
    ]

    for chat in history:
        st_message(**chat)


# All functions called from main_bot() are here
try:
    if st.session_state["link_submitted"] == "Done":
        st.set_page_config(page_title="docuGPT", page_icon=":robot_face:", layout="centered")
        main_bot()
except KeyError:
    st.set_page_config(page_title="docuGPT", page_icon=":robot_face:", layout="centered")
    st.title("Please submit a link first in Home. :smile:") 





