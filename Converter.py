import streamlit as st
from PIL import Image
import io

st.title("Image to Grayscale")
st.subheader('Convert Image to Grayscale')

with st.expander('Upload Image'):
    file = st.file_uploader('Upload Image', type=['png', 'jpg', 'jpeg'])

if file:
    image = Image.open(file)
    grayscale = image.convert('L')
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