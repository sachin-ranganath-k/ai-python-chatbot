import streamlit as st

#sets header for app
st.header("Chatbot App");

#sidebar for app
with st.sidebar:
    st.title("Your documents")
    file = st.file_uploader("Upload your PDF file", type='pdf')
    st.markdown("Upload file and start asking questions")
