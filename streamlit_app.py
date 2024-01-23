import streamlit as st
import base64

st.title('PDF Viewer with PDF.js')

# File uploader widget
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

# Function to convert file data to base64
def to_base64(data):
    return base64.b64encode(data.read()).decode('utf-8')

if uploaded_file is not None:
    pdf_base64 = to_base64(uploaded_file)
    pdf_viewer_html = f'''
    <html>
    <head>
      <script src="https://mozilla.github.io/pdf.js/build/pdf.js"></script>
    </head>
    <body>
      <div id="pdf-viewer"></div>
      <script>
        var loadingTask = pdfjsLib.getDocument({{data: atob("{pdf_base64}")}});
        loadingTask.promise.then(function(pdf) {{
          console.log('PDF loaded');
          
          // Get div container
          var container = document.getElementById('pdf-viewer');

          // Loop over each page in the PDF
          for (let pageNum = 1; pageNum <= pdf.numPages; pageNum++) {{
            pdf.getPage(pageNum).then(function(page) {{
              console.log('Page loaded');
              
              var scale = 1.0;
              var viewport = page.getViewport({{scale: scale}});
              var canvas = document.createElement('canvas');
              canvas.style.display = "block";
              var context = canvas.getContext('2d');
              canvas.height = viewport.height;
              canvas.width = viewport.width;

              // Render PDF page into canvas context
              var renderContext = {{
                canvasContext: context,
                viewport: viewport
              }};
              var renderTask = page.render(renderContext);
              renderTask.promise.then(function () {{
                console.log('Page rendered');
              }});

              // Append canvas to the container
              container.appendChild(canvas);
            }});
          }}
        }}, function (reason) {{
          // PDF loading error
          console.error(reason);
        }});
      </script>
    </body>
    </html>
    '''

    # Display the PDF
    st.components.v1.html(pdf_viewer_html, height=800, scrolling=True)