import streamlit as st
from PyPDF2 import PdfReader 

st.set_page_config(
    page_title="Chatbot App",
    layout="centered",  # Better for mobile responsiveness
)

st.markdown("""
<!-- Force desktop view on mobile -->
<meta name="viewport" content="width=1024">
""", unsafe_allow_html=True)

# Custom CSS to hide various elements
hide_streamlit_elements = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stDeployButton {display:none;} /* Hides the Deploy button */
.stApp [data-testid="stToolbar"] {display: none;} /* Hides the entire toolbar including share/star */
.stApp [data-testid="stDecoration"] {display: none;} /* Hides the "Made with Streamlit" footer */
.viewerBadge_container__1QSob {display: none;} /* Hides the "Made with Streamlit" badge */
._terminalButton_rix23_138 [data-testid="manage-app-button"] {display: none;}
</style>
"""
st.markdown(hide_streamlit_elements, unsafe_allow_html=True)

#sets header for app
st.header("Chatbot App");

#sidebar for app
with st.sidebar:
    st.title("Your documents")
    file = st.file_uploader("Upload your PDF file", type='pdf')
    st.markdown("Upload file and start asking questions")

#Extract text from pdf file
if file is not None:
    file_reader = PdfReader(file)
    text=''
    for page in file_reader.pages:
        text+=page.extract_text()
        st.write(text)
