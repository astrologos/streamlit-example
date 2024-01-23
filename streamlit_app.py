import streamlit as st
import base64

st.title('PDF Viewer')

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    # Convert the file to base64
    pdf_file = uploaded_file.read()
    b64_pdf = base64.b64encode(pdf_file).decode('utf-8')

    # Embedding the PDF in an HTML iframe
    pdf_display = f'''
    <iframe width="700" height="1000" src="data:application/pdf;base64,{b64_pdf}" type="application/pdf"></iframe>
    '''
    st.markdown(pdf_display, unsafe_allow_html=True)