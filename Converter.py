import streamlit as st
from PIL import Image
import io

st.title("Grayscale Converter")
st.write('Select image file to convert into grayscale image')

with st.expander('Upload Image'):
    file = st.file_uploader('Upload Image', type=['png', 'jpg', 'jpeg'])

if file:
    image = Image.open(file)
    grayscale = image.convert('L')
    col1, col2 = st.columns(2)
    with col1:
        st.write("Result:")
        st.image(grayscale)

        img_byte_arr = io.BytesIO()
        grayscale.save(img_byte_arr, format=image.format)
        img_byte_arr = img_byte_arr.getvalue()

        st.download_button(
            label='Download Image',
            data=img_byte_arr,
            file_name=f"download_image.{image.format.lower()}",
            mime=f"image/{image.format.lower()}"
        )

    with col2:
        st.write("original:")
        st.image(image)