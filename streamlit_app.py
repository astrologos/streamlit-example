import streamlit as st
import base64

st.title('Responsive PDF Viewer')

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    # Convert the file to base64
    pdf_file = uploaded_file.read()
    b64_pdf = base64.b64encode(pdf_file).decode('utf-8')

    # HTML for the responsive iframe
    pdf_display = f'''
    <html>
    <head>
        <style>
            .pdf-container {{
                height: 80vh; /* 80% of the viewport height */
                width: 100%; /* Full width */
                overflow: auto; /* Scrollbar if needed */
                position: relative; /* For positioning the iframe */
            }}
            .pdf-container iframe {{
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
            }}
        </style>
    </head>
    <body>
        <div class="pdf-container">
            <iframe src="data:application/pdf;base64,{b64_pdf}" frameborder="0" scrolling="yes"></iframe>
        </div>
    </body>
    </html>
    '''
    st.markdown(pdf_display, unsafe_allow_html=True)