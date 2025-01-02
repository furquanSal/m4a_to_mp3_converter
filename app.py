import streamlit as st
from pydub import AudioSegment
from io import BytesIO
from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

def convert_m4a_to_mp3(m4a_file):
    """
    Converts an m4a audio file to mp3 format.
    :param m4a_file: Uploaded m4a file object
    :return: Converted mp3 file object
    """
    audio = AudioSegment.from_file(m4a_file, format="m4a")
    mp3_file = BytesIO()
    audio.export(mp3_file, format="mp3")
    mp3_file.seek(0)
    return mp3_file

# Load Lottie animations
loading_animation = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_jcikwtux.json")
# success_animation = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_ydo1amjm.json")

# Streamlit application
st.markdown(
    """
    <style>
        .main {
            background-color: #f0f8ff;
            color: #333;
        }
        .title {
            text-align: center;
            color: #007BFF;
        }
        .footer {
            text-align: center;
            font-size: 14px;
            color: #666;
            margin-top: 50px;
        }
        hr {
            border: 1px solid #ddd;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🎵 M4A to MP3 Converter")
st.markdown(
    """<div class="title">Upload an M4A audio file to convert it to MP3 format quickly and easily!</div>""",
    unsafe_allow_html=True,
)

uploaded_file = st.file_uploader("Choose an M4A file", type="m4a")
if uploaded_file is not None:
    filename = uploaded_file.name.rsplit(".", 1)[0]
    with st.spinner("Converting..."):
        st_lottie(loading_animation, height=150, key="loading")
        try:
            mp3_file = convert_m4a_to_mp3(uploaded_file)
            st.success("🎉 Conversion successful!")
            # st_lottie(success_animation, height=150, key="success")

            # Display audio player
            # st.audio(mp3_file, format="audio/mp3", start_time=0, autoplay=True)

            # Download button for the converted file
            st.download_button(
                label="⬇️ Download MP3 File",
                data=mp3_file,
                file_name=f"{filename}_converted.mp3",
                mime="audio/mp3",
                key="download_button"
            )
        except Exception as e:
            st.error(f"An error occurred during conversion: {e}")
else:
    st.info("Please upload an M4A file to start the conversion.")

# Footer
st.markdown(
    """
    <hr>
    <div class="footer">
        &copy; All rights reserved 2025. Developed by 
        <a href="https://mohammedfurquansaleem.in" target="_blank" style="text-decoration: none; color: #007BFF;">
            Mohammed Furqan Saleem
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)