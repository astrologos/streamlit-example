import streamlit as st
import base64

st.title('Responsive PDF Viewer')

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    # Convert the file to base64
    pdf_file = uploaded_file.read()
    b64_pdf = base64.b64encode(pdf_file).decode('utf-8')

    # HTML and JavaScript for a responsive PDF viewer
    pdf_display = f'''
    <html>
    <head>
        <script>
            function resizeIframe(obj) {{
                obj.style.height = obj.contentWindow.document.documentElement.scrollHeight + 'px';
            }}
        </script>
    </head>
    <body>
        <div style="overflow-y: auto; height: calc(100vh - 150px);">
            <iframe src="data:application/pdf;base64,{b64_pdf}" 
                    style="width:100%; border:none;" 
                    onload="resizeIframe(this)" 
                    scrolling="yes" 
                    id="pdf-iframe"></iframe>
        </div>
    </body>
    </html>
    '''
    st.markdown(pdf_display, unsafe_allow_html=True)