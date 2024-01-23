import streamlit as st
import base64

st.title('Responsive PDF Viewer')

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    # Convert the file to base64
    pdf_file = uploaded_file.read()
    b64_pdf = base64.b64encode(pdf_file).decode('utf-8')

    # HTML to embed PDF in a responsive container
    pdf_display = f'''
    <div style="height: 80vh; width: 100%; overflow-y: scroll;">
        <iframe width="100%" height="100%" src="data:application/pdf;base64,{b64_pdf}" type="application/pdf"></iframe>
    </div>
    '''
    st.markdown(pdf_display, unsafe_allow_html=True)