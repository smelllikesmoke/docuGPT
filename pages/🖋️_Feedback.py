import streamlit as st
from database import add_feedback

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def about_desc(): # put all descitpion for about me here
    st.write("we;re antematter")

st.set_page_config(page_title="docuGPT", page_icon=":robot_face:", layout="centered")
local_css("/home/saad/extra/lablab-hackaton/streamlit_prac/pages/style.css")

st.markdown("## Please leave your feedback below. :smile:")
st.text_area(label="Feedback below", label_visibility= "hidden", key="feedback", placeholder="Type your feedback here...")
if st.button("Submit :heart:"):
    add_feedback(st.session_state.feedback)
    st.success("✅ Feedback submitted successfully. ✅")
    if "feedback_submitted" not in st.session_state:
        st.session_state["feedback_submitted"] = "Done"

with st.expander("About us!"):

    ante_matter_link = '[Antematter](https://www.antematter.io)'
    st.markdown(" ### We're {Antematter}.".format(Antematter= ante_matter_link), unsafe_allow_html=True)
    about_desc()    
















