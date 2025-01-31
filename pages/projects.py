import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Hema Priya Pothumarthi - Portfolio", page_icon=":robot:", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>

            .big-font {
            font-size:50px !important;
            font-weight: bold;
            }
            .medium-font {
            font-size:20px !important;
            }
            .small-font {
            font-size:16px !important;
            }
            .header {
            background-color: #a9a095;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
            }
</style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <style>
    
    [data-testid="stAppViewContainer"] {
        background-color: #bcb4a1;
    }
    </style>
    """,
    unsafe_allow_html=True
)



# Projects Section
st.markdown('<div class="header"><h2 class="medium-font">Projects</h2></div>', unsafe_allow_html=True)
st.markdown("""
<p class="small-font">
    <strong>Development of an Automated Guided Vehicle (AGV) for Lawn Mowing</strong><br>
    - Led the project by modeling the AGV in Fusion360 and tested simulations in Simulink to optimize and validate AGV performance.<br>
    - Actively integrated the mechanical and electrical components to the 3D printed prototype to program through Arduino IDE to develop a fully functional autonomous lawn mower.<br><br>
</p>
            <p>    
    <strong>What’s For Dinner?</strong><br>
    - Developed a vegetable detection pipeline using DE-VIT model, increasing object detection accuracy from 60% to 85% through the creation of a novel dataset with more classes.<br>
    - Created a spice detection pipeline using label detection and Google OCR, combining results to curate ingredient lists for customized recipe generation via ChatGPT increasing functionality.<br>
    - Built an interactive web application to collect user inputs and deliver tailored recipes, enhancing user engagement.<br><br>
  </p>
<p>  
    <strong>Designing and Building an All-Terrain-Vehicle: BAJA SAE</strong><br>
    - Designed and constructed an all-terrain vehicle with a focus on designing the suspension system, improving off-road performance, stability, and durability.<br>
    - Played a key role in Green BAJA initiatives, reducing the vehicle’s carbon footprint by 13% and fuel consumption by 5.5%.
</p>
""", unsafe_allow_html=True)