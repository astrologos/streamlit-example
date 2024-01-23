import streamlit as st
import fitz  # PyMuPDF
import io
from PIL import Image

st.title('PDF Viewer with Drawable Canvas')

# File uploader widget
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    # Load the PDF
    pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    
    for page_num in range(len(pdf_document)):
        # Get the page
        page = pdf_document.load_page(page_num)

        # Convert it to an image
        pix = page.get_pixmap()
        image_data = pix.tobytes()
        image = Image.open(io.BytesIO(image_data))

        # Display image in a canvas
        st.image(image, caption=f"Page {page_num + 1}")
        canvas_result = st_canvas(
            fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
            stroke_width=3,
            stroke_color="#000000",
            background_color="#eee",
            background_image=Image.open(image),
            update_streamlit=True,
            height=300,
            drawing_mode="freedraw",
            key=f"canvas{page_num}",
        )
        if canvas_result.image_data is not None:
            st.image(canvas_result.image_data)

    pdf_document.close()