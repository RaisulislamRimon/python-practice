# this is a camera opening and take image/photo with python project
# to run this file, paste this command to the powershell:
# streamlit run bonus19.py
import streamlit as st
from PIL import Image

with st.expander("Start Camera"):
    # start the camera
    camera_image = st.camera_input("Camera")
    # print('camera_image', camera_image)

if camera_image:
    # create a pillow image instance
    img = Image.open(camera_image)
    # print('img', img)

    # convert the pillow image to grayscale
    gray_img = img.convert("L")
    # print('gray_img', gray_img)

    # render the grayscale image to the web page
    st.image(gray_img)
