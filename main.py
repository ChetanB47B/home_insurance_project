import base64

import streamlit as st

from data_extraction import data_filter
import streamlit_authenticator as stauth

st.title("Property inspection !!")

uploaded_image = st.file_uploader("Upload an image file", type=["jpg", "jpeg", "png"])
if uploaded_image is not None:
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
    option = st.selectbox(
        'Select the description for the provided image',
        ('Exterior',))
        # ('Animal Present', 'Roof', 'Chimney', 'Exterior', 'Foundation', 'Porches', 'External damage'))

    st.write('You selected:', option)
    encoded_image = base64.b64encode(uploaded_image.read()).decode()
    result = data_filter(option, encoded_image)
    st.write(result)
