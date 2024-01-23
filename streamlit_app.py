import streamlit as st
import base64

st.title('Viewport-Fitted and Zoomable PDF Viewer')

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    # Convert the file to base64
    pdf_file = uploaded_file.read()
    b64_pdf = base64.b64encode(pdf_file).decode('utf-8')

    # HTML and JavaScript for zoomable PDF viewer and control buttons
    pdf_display = f'''
    <html>
    <head>
        <script>
            function zoomIn() {{
                var iframe = document.getElementById('pdf-iframe');
                var currWidth = iframe.clientWidth;
                iframe.style.width = (currWidth + 100) + "px";
            }}
            function zoomOut() {{
                var iframe = document.getElementById('pdf-iframe');
                var currWidth = iframe.clientWidth;
                if(currWidth > 100) {{
                    iframe.style.width = (currWidth - 100) + "px";
                }}
            }}
            function resetZoom() {{
                var iframe = document.getElementById('pdf-iframe');
                iframe.style.width = "100%";
            }}
        </script>
    </head>
    <body>
        <div style="text-align: center;">
            <button onclick="zoomIn()">Zoom In</button>
            <button onclick="zoomOut()">Zoom Out</button>
            <button onclick="resetZoom()">Reset Zoom</button>
        </div>
        <div style="height: calc(100vh - 150px); overflow-y: auto;">
            <iframe id="pdf-iframe" src="data:application/pdf;base64,{b64_pdf}" style="width:100%; height:100%;" frameborder="0" scrolling="yes"></iframe>
        </div>
    </body>
    </html>
    '''
    st.markdown(pdf_display, unsafe_allow_html=True)