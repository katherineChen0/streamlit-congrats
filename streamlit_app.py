from pathlib import Path
import json
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain

#Directories and file paths
THIS_DIR = Path(__file__).resolve().parent
CSS_FILE = THIS_DIR / "style" / "style.css"
ASSETS = THIS_DIR / "assets"
LOTTIE_ANIMATION = ASSETS / "animation_holiday.json"

#function to load and display the Lottie animation
def load_lot_animation(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

#function to apply snowfall effect
def run_snow_animation():
    rain(emoji="❄️", font_size=20, falling_speed=5, animation_length="infinite")

#function to get the name from query parameters
def get_person_name():
    query_params = st.experimental_get_query_params()
    return query_params.get("name", ["Friend"])[0]

#page configuration
st.set_page_config(page_title="Congrats!", page_icon =" 😁 ")

#run snowfall animation
run_snow_animation()

#apply custom CSS
with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#display header with personalized name
PERSON_NAME = get_person_name()
st.header(f"Congrats, {PERSON_NAME}! 😁 ", anchor=False)

#display Lottie animation
lottie_animation = load_lot_animation(LOTTIE_ANIMATION)
st_lottie(lottie_animation, key="lottie-holiday", height=300)

#personalized message
st.markdown(
    f"Dear {PERSON_NAME}, i am so proud of you for getting through another year. "
)
