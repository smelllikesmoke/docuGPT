import streamlit as st
from streamlit_chat import message as st_message
from middleware import main


# All calls (to other functions) from this function
def main_bot():
    st.set_page_config(page_title="docuGPT", page_icon=":robot_face:", layout="centered")
    st.title("Go ham, the bot is all yours now.")
    # st.text_input(label="Enter your message here: ", key="bot_chat", placeholder="Type your message here...", on_change=main(st.session_state["link"], st.session_state["bot_chat"]))
    st.text_input(label="Enter your message here: ", key="ques", placeholder="Type your message here...")
    print(st.session_state["ques"])
    with st.spinner("Loading..."):
        st.button("Send :rocket:", on_click=main) 
        for i, chat in enumerate(st.session_state.history):
            st_message(**chat, key=str(i)) #unpacking

    
# All functions called from main_bot() are here
try:
    if st.session_state["link_submitted"] == "Done":
        main_bot()
except KeyError:
    st.set_page_config(page_title="docuGPT", page_icon=":robot_face:", layout="centered")
    st.title("Please submit a link first in Home. :smile:") 





