import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Hema Priya Pothumarthi - Portfolio", page_icon=":robot:", layout="wide")

# Custom CSS for styling

st.markdown(
    
    """
    <style>
    
    [data-testid="stAppViewContainer"] {
        background-color: #171D1C;
        padding: 0;
    }
    
    [data-testid="stMain"] {
        background-color: #171D1C;
        padding: 0px 20px 50px 20px;
    }

    .main .block-container {
        padding-top: 20px !important; /* Minimal top padding */
        padding-bottom: 0px;
    }
    </style>
    """,
    unsafe_allow_html=True
) 


st.markdown(
    """
    <style>
        .nav-link {
            text-decoration: none;
            font-size: 25px;
            
            /*padding-top: 10px !important;*/
            margin-bottom: 10px !important;
            border-radius: 5px;
            background-color: #BC7C9C;
            color: black;
        }
        .nav-link:hover {
            background-color: #A96DA3;
        }

        [data-testid="stSidebar"] {
        display: none !important;
        }

        [data-testid="collapsedControl"] {
        display: none !important;
        }

        .css-1d391kg {
        display: none !important;
        }

        [data-testid="stSidebarNav"] {
        display: none !important;
    }

        .big-font {
        font-size: 50px !important;
        font-weight: bold;
        color: #A96DA3 !important;
        /*margin-top: 40px !important; */
        }
        .medium-font {
            font-size: 20px !important;
            color: #ffffff !important;
        }
        .hero-quote {
        font-size: 50px !important;
        font-weight: 300;
        color: #ffffff !important;
        padding-top: 160px !important; 
        margin-bottom: 40px;
        line-height: 1.3;
        font-style: italic;
        }
        .small-font {
            font-size: 16px !important;
            color: #ffffff !important;
        }
        .small-font a {
        color: #BC7C9C !important;
        text-decoration: underline;
        }
        .header {
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)



with st.container():

    # Header row with name and navigation
    header_col1, header_col2 = st.columns([2, 1])
    
    with header_col1:
        st.markdown('<h1 class="big-font">Hema Priya Pothumarthi</h1>', unsafe_allow_html=True)
    
    with header_col2:
        st.markdown("""
        <div style="text-align: right; margin-top: 30px;">
            <a href="/projects" style="color: #BC7C9C; text-decoration: none; margin: 0 15px; font-size: 30px; font-weight: 500;">Projects</a>
            <a href="/interests" style="color: #BC7C9C; text-decoration: none; margin: 0 15px; font-size: 30px; font-weight: 500;">Interests</a>
            <a href="/passions" style="color: #BC7C9C; text-decoration: none; margin: 0 15px; font-size: 30px; font-weight: 500;">Passions</a>
        </div>
        """, unsafe_allow_html=True)

    # Content row with quote and image
    image = Image.open("picture.jpg")
    content_col1, content_col2 = st.columns([2, 1])
    
    with content_col1:
        st.markdown(
            """
            <p class="hero-quote">
            "Empathy in design,<br>
            technology in action,<br>
            sustainability at the core."
            </p>
            """,
            unsafe_allow_html=True
            )
    with content_col2:
        st.image(image, use_container_width=True)
 
    
    



    st.markdown('<p class="medium-font">Robotics Engineer | MS in Robotics at University of Pennsylvania</p>', unsafe_allow_html=True)
    st.markdown('<p class="small-font">Email: hemapothumarthi@gmail.com | Phone: (267)-261-2654 | <a href="https://github.com/hpriyap">GitHub</a> | <a href="https://www.linkedin.com/in/hema-priya-pothumarthi-2752001p26">LinkedIn</a></p>', unsafe_allow_html=True)
    st.markdown("""
                <h2 class="medium-font" style="margin-top: 10px;">About Me</h2>
                <p class="small-font" style="margin-top: -10px;">
                I am a passionate Robotics Engineer currently pursuing my Master's in Robotics at the University of Pennsylvania. 
                My expertise lies in robotics, machine learning, computer vision, and human-computer interaction. 
                I have hands-on experience in developing and optimizing robotic systems, and I am always eager to take on new challenges in the field of robotics and automation.
                </p>
                """, unsafe_allow_html=True)
    
    # Education Section
    st.markdown('<div class="header"><h2 class="medium-font">Education</h2></div>', unsafe_allow_html=True)
    st.markdown("""
    <p class="small-font">
        <strong>University of Pennsylvania, Philadelphia, PA</strong><br>
        Master of Science in Robotics (MSE)<br>
        Aug 2023 – Dec 2025<br>
        Relevant Coursework: Machine Learning, Computer Vision, Linear Systems Theory, Human-Computer Interaction<br>
        GPA: 3.67/4.00<br><br>
    </p>
    <p>   
        <strong>VNR Vignana Jyothi Institute of Technology, Hyderabad, India</strong><br>
        Bachelor of Technology in Mechanical Engineering<br>
        Aug 2019 – June 2023<br>
        GPA: 3.65/4.00
    </p>
    """, unsafe_allow_html=True)

    # Technical Skills Section
    st.markdown('<div class="header"><h2 class="medium-font">Technical Skills</h2></div>', unsafe_allow_html=True)
    st.markdown("""
    <p class="small-font">
        <strong>Platforms/Tools/Frameworks:</strong> Solidworks, AutoCAD, Roboguide, Gazebo, MATLAB, PyTorch, NumPy, Pandas<br>
        <strong>Operating Systems:</strong> Linux (Ubuntu), ROS, ROS2<br>
        <strong>Programming Languages:</strong> Python, C, C++
    </p>
    """, unsafe_allow_html=True)

    # Experience Section
    st.markdown('<div class="header"><h2 class="medium-font">Experience</h2></div>', unsafe_allow_html=True)
    st.markdown("""
    <p class="small-font">
        <strong>Ava Robotics, Somerville, MA</strong><br>
        Robotics Engineer Intern<br>
        Feb 2024 – June 2024<br>
        - Developed troubleshooting protocols for Ava robot systems, resulting in a 11% performance improvement.<br>
        - Updated Ava Robot’s OS and optimized resources, leading to smoother and faster task execution.<br>
        - Developed APIs for communication between robot components and external systems, boosting system integration and task automation.<br><br>
    </p>
    <p>   
        <strong>Swan Turbine Services, Hyderabad, India</strong><br>
        Engineering Intern<br>
        May 2023 – July 2023<br>
        - Assisted in managing production processes and inventory control, improving resource allocation efficiency.<br>
        - Involved in departmental operations and project management, enhancing cross-functional workflow.<br><br>
    </p>
    <p>   
        <strong>FANUC, India</strong><br>
        Trainee<br>
        Oct 2022 – Nov 2022<br>
        - Trained in programming and simulating multiple FANUC robots using Roboguide software.<br>
        - Applied this knowledge to calibrate and train a 6-axis SCARA Robot for multiple pick-and-place and assembly operations.<br><br>
    </p>
    <p>    
        <strong>University of Pennsylvania</strong><br>
        Graduate Monitor, Weingarten Tutoring Center<br>
        Aug 2024 – Present<br>
        - Enhanced tutoring experience by troubleshooting system performance issues and optimizing equipment use.<br>
        - Increased drop-in tutoring center outreach through student interactions, enhancing the academic support system.
    </p>
    """, unsafe_allow_html=True)



    # Leadership Section
    st.markdown('<div class="header"><h2 class="medium-font">Leadership</h2></div>', unsafe_allow_html=True)
    st.markdown("""
    <p class="small-font">
        <strong>ROTARACT - Youth Wing of Rotary International, District 3150, India</strong><br>
        - Organized community service events focusing on women’s menstrual health awareness and conducted educational and entertainment sessions for children across 4 orphanages.<br>
        - Fostered camaraderie and cohesion within the club by orchestrating 5 fellowship events.<br><br>
    </p>
                <p>    
        <strong>Livewire Dance Crew, Collegiate Dance Club of VNRVJIET, Hyderabad</strong><br>
        - Managed and organized a team of 40 dancers, leading Livewire Dance Crew to multiple victories and enhancing its reputation.<br>
        - Handled finances, edited audio tracks, and managed social media ensuring efficient operations and increased crew reach.
    </p>
    """, unsafe_allow_html=True)

    # Footer Section
    st.markdown("""
    <p class="small-font" style="text-align: center;">
        &copy; 2024 Hema Priya Pothumarthi. All rights reserved.
    </p>
    """, unsafe_allow_html=True)

