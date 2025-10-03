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
            font-size: 20px;
            
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

st.markdown("""
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
""", unsafe_allow_html=True)

with st.container():

    # Header row with name and navigation
    header_col1, header_col2 = st.columns([2, 1])
    
    with header_col1:
        st.markdown('<h1 class="big-font">Hema Priya Pothumarthi</h1>', unsafe_allow_html=True)
    
    with header_col2:
        st.markdown("""
        <div style="text-align: right; margin-top: 30px;">
            <a href="/projects" style="color: #BC7C9C; text-decoration: none; margin: 0 10px; font-size: 22px; font-weight: 500;">Projects</a>
            <a href="/interests" style="color: #BC7C9C; text-decoration: none; margin: 0 10px; font-size: 22px; font-weight: 500;">Interests</a>
            <a href="/passions" style="color: #BC7C9C; text-decoration: none; margin: 0 10px; font-size: 22px; font-weight: 500;">Passions</a>
        </div>
        """, unsafe_allow_html=True)

    # Content row with quote and image
    
    
    try:
        image = Image.open("picture.jpg")
        # Resize image while maintaining aspect ratio and quality
        image = image.resize((400, int(400 * image.height / image.width)), Image.Resampling.LANCZOS)
    except FileNotFoundError:
        image = None
    
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
 
    

    
    
    st.markdown("""
                <h2 class="medium-font" style="margin-top: 10px;">About Me</h2>
                <p class="small-font" style="margin-top: -10px;">
                I am a passionate Robotics Engineer currently pursuing my Master's in Robotics at the University of Pennsylvania where I focus on bridging the gap between intelligent autonomy and real-world deployment. 
                My core strength lies at the intersection of robotics, machine learning, computer vision and mechanical design. 
                I bring a collaborative and system-level mindset, to cross-functional teams of mechanical, electrical, and software engineers to design scalable, reliable robotics solutions. 
                Above all, I believe robotics should be people-centered, field-ready, and designed with empathy. 
                My goal is to build intelligent machines that not only move through the world — but do so purposefully, efficiently, and safely alongside humans.
                </p>
                """, unsafe_allow_html=True)
    
    # Education Section
    st.markdown('<div class="header"><h2 class="medium-font">Education</h2></div>', unsafe_allow_html=True)
    st.markdown("""
    <p class="small-font">
        <strong>University of Pennsylvania, Philadelphia, PA</strong><br>
        Master of Science in Robotics (MSE)<br>
        Relevant Coursework: Machine Learning, Computer Vision, Linear Systems Theory, Human-Computer Interaction<br>
        
    </p>
    <p class="small-font">   
        <strong>VNR Vignana Jyothi Institute of Technology, Hyderabad, India</strong><br>
        Bachelor of Technology in Mechanical Engineering<br>
        
    </p>
    """, unsafe_allow_html=True)



# Education Section Title
st.markdown("""
    <div style="padding: 40px 0 30px 0;">
        <h2 style="font-size: 48px; font-weight: 800; color: #F3A5C8; text-align: center;">Education</h2>
    </div>
""", unsafe_allow_html=True)

edu_col1, edu_col2 = st.columns(2)

with edu_col1:
    st.markdown("""
        <div class="aos-box" data-aos="fade-up" style="background-color: #2D2A32; border-radius: 15px; padding: 25px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4); margin-bottom: 20px;">
            <h3 style="color: #F3A5C8; font-weight: bold;">Robotics Engineer</h3>
            <p class="small-font">
                <strong>University of Pennsylvania, Philadelphia, PA</strong><br>
                Master of Science in Robotics (MSE)<br>
                Aug 2023 – Dec 2025<br>
                GPA: 3.67/4.00<br>
                <em>Relevant Coursework:</em> Machine Learning, Computer Vision, Linear Systems Theory, HCI
            </p>
        </div>
    """, unsafe_allow_html=True)

with edu_col2:
    st.markdown("""
        <div class="aos-box" data-aos="fade-up" data-aos-delay="200" style="background-color: #2D2A32; border-radius: 15px; padding: 25px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4); margin-bottom: 20px;">
            <h3 style="color: #F3A5C8; font-weight: bold;">Mechanical Engineer</h3>
            <p class="small-font">
                <strong>VNR Vignana Jyothi Institute of Technology, Hyderabad, India</strong><br>
                Bachelor of Technology in Mechanical Engineering<br>
                Aug 2019 – June 2023<br>
                GPA: 3.65/4.00
            </p>
        </div>
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
    <p class="small-font">   
        <strong>Swan Turbine Services, Hyderabad, India</strong><br>
        Engineering Intern<br>
        May 2023 – July 2023<br>
        - Assisted in managing production processes and inventory control, improving resource allocation efficiency.<br>
        - Involved in departmental operations and project management, enhancing cross-functional workflow.<br><br>
    </p>
    <p class="small-font">   
        <strong>FANUC, India</strong><br>
        Trainee<br>
        Oct 2022 – Nov 2022<br>
        - Trained in programming and simulating multiple FANUC robots using Roboguide software.<br>
        - Applied this knowledge to calibrate and train a 6-axis SCARA Robot for multiple pick-and-place and assembly operations.<br><br>
    </p>
    <p class="small-font">    
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
    <p class="small-font">    
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


# Run AOS script at the end so it doesn't break layout
st.markdown("""
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        AOS.init({
            duration: 1000,
            once: true
        });
    </script>
""", unsafe_allow_html=True)
