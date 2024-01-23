import streamlit as st
import base64

st.title('Viewport-Fitted PDF Viewer')

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    # Convert the file to base64
    pdf_file = uploaded_file.read()
    b64_pdf = base64.b64encode(pdf_file).decode('utf-8')

    # HTML to embed PDF in a fully responsive container
    pdf_display = f'''
    <div style="height: calc(100vh - 150px); overflow-y: auto;">
        <iframe src="data:application/pdf;base64,{b64_pdf}" style="width:100%; height:100%;" frameborder="0" scrolling="yes"></iframe>
    </div>
    '''
    st.markdown(pdf_display, unsafe_allow_html=True)