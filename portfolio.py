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

        html {
        scroll-behavior: smooth;
        }

        /* Fade-in scroll animation */
        .fade-in {
        opacity: 0;
        transform: translateY(40px);
        animation: fadeInUp 1s ease forwards;
        animation-delay: 0.2s;
        visibility: visible;
        }

        .fade-in.delay {
        animation-delay: 0.6s;
        }

        @keyframes fadeInUp {
        from {
        opacity: 0;
        transform: translateY(40px);
        }
        to {
        opacity: 1;
        transform: translateY(0);
        }
        }
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




with st.container():

    
    
    # Header row with name and navigation
    header_col1, header_col2 = st.columns([2, 1])
    
    with header_col1:
        st.markdown('<h1 class="big-font">Hema Priya Pothumarthi</h1>', unsafe_allow_html=True)
    
    with header_col2:
        
        st.markdown("""
                    <div style="text-align: right; margin-top: 30px;">
                    <a href="#experience-section" style="color: #BC7C9C; text-decoration: none; margin: 0 10px; font-size: 22px; font-weight: 500;">Experience</a>
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
st.markdown('<div class="header"><h2 "color: #BC7C9C; font-size: 24px;">Education</h2></div>', unsafe_allow_html=True)

edu_col1, edu_col2 = st.columns(2)

with edu_col1:
    st.markdown("""
                <div style="background-color: #2D2A32; border-radius: 15px; padding: 25px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2); margin-bottom: 20px;">
                <h3 style="color: #F5F5F5; font-weight: bold;">Robotics Engineering</h3>
                <p style="color: #BC7C9C; font-size: 16px;" >
                <strong>University of Pennsylvania, Philadelphia, PA</strong><br>
                Master of Science<br>
        </p>
    </div>
    """, unsafe_allow_html=True)



with edu_col2:
    st.markdown("""
    <div style="background-color: #2D2A32; border-radius: 15px; padding: 25px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2); margin-bottom: 20px;">
        <h3 style="color: #F5F5F5; font-weight: bold;">Mechanical Engineering</h3>
        <p style="color: #BC7C9C; font-size: 16px;">
            <strong>VNRVJIET, Hyderabad, India</strong><br>
            Bachelor of Technology<br>
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


# Add this line above the Experience heading
st.markdown('<div id="Experience"></div>', unsafe_allow_html=True)

# Experience Section
st.markdown('<div class="header"><h2 "color: #BC7C9C; font-size: 24px;">Experience</h2></div>', unsafe_allow_html=True)

# Shared style
tile_style = """
    background-color: #2D2A32; 
    border-radius: 20px; 
    padding: 25px; 
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    margin-bottom: 20px;
"""

# Row 1 – Ava Robotics & Swan Turbine
exp_row1_col1, exp_row1_col2 = st.columns(2)

with exp_row1_col1:
    st.markdown(f"""
    <div style="{tile_style}">
        <h3 style="color: white; font-weight: bold;">Robotics Engineer Intern</h3>
        <p style="color: #BC7C9C; font-size: 16px;">
            Ava Robotics, Somerville, MA<br>
        </p>
        <p style="color: #F5F5F5; font-size: 16px;">
            Developed and deployed system diagnostics and runtime enhancements for Ava’s autonomous telepresence robots. 
            Improved OS performance, reduced latency, and streamlined remote system access by designing secure APIs for telemetry and over-the-air updates. 
            Collaborated with cross-functional teams to ensure the robots operated reliably and efficiently in real-world environments.
        </p>
    </div>
    """, unsafe_allow_html=True)

with exp_row1_col2:
    st.markdown(f"""
    <div style="{tile_style}">
        <h3 style="color: white; font-weight: bold;">Engineering Intern</h3>
        <p style="color: #BC7C9C; font-size: 16px;">
            Swan Turbine Services, Hyderabad, India<br>
        </p>
        <p style="color: #F5F5F5; font-size: 16px;">
            Conducted market analysis by researching competitors and identifying marketing gaps to enhance the company’s global outreach. 
            Explored potential strategic partnerships within the industry.
            Collaborated across departments to map end-to-end workflows, identify inefficiencies, and establish clearer roles and responsibilities — resulting in improved cross-functional communication and operational efficiency.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Row 2 – FANUC & UPenn Monitor
exp_row2_col1, exp_row2_col2 = st.columns(2)

with exp_row2_col1:
    st.markdown(f"""
    <div style="{tile_style}">
        <h3 style="color: white; font-weight: bold;">Trainee</h3>
        <p style="color: #BC7C9C; font-size: 16px;">
            FANUC, India<br>
        </p>
        <p style="color: #F5F5F5; font-size: 16px;">
            Learned programming and simulation of FANUC robots using Roboguide. Calibrated SCARA robots for real-world pick-and-place and assembly use cases.
        </p>
    </div>
    """, unsafe_allow_html=True)

with exp_row2_col2:
    st.markdown(f"""
    <div style="{tile_style}">
        <h3 style="color: white; font-weight: bold;">Graduate Monitor</h3>
        <p style="color: #BC7C9C; font-size: 16px;">
            Weingarten Tutoring Center, University of Pennsylvania<br>
        </p>
        <p style="color: #F5F5F5; font-size: 16px;">
            Troubleshoot technical issues, enhance equipment utilization, and build student awareness to increase outreach of tutoring services.
        </p>
    </div>
    """, unsafe_allow_html=True)





# Beyond Engineering Section
st.markdown('<div class="header"><h2 "color: #BC7C9C; font-size: 24px;">Beyond Engineering</h2></div>', unsafe_allow_html=True)


# ROTARACT: Text Left, Image Right
rotaract_col1, rotaract_col2 = st.columns([3, 2])

with rotaract_col1:
    st.markdown("""
        <div style="padding: 30px 40px;">
            <h3 style="color: #A96DA3; font-weight: bold;">ROTARACT - Youth Wing of Rotary International</h3>
            <p style="color: #F5F5F5; font-size: 16px;"><strong>District 3150, India</strong></p>
            <p style="color: #F5F5F5; font-size: 16px;">
            As a committed member of ROTARACT, I led impactful social initiatives that addressed women’s health education and youth engagement. 
            I spearheaded menstrual hygiene awareness drives, delivering educational sessions and distributing hygiene kits in under-resourced communities. 
                I also organized interactive, play-based learning sessions in four orphanages, helping foster curiosity and joy among the children. Beyond outreach, I strengthened internal club spirit by planning and executing five fellowship events that deepened team cohesion and collective impact.
            </p>
        </div>
    """, unsafe_allow_html=True)

with rotaract_col2:
    try:
        image = Image.open("PXL_20220403_083203462.jpg")
        st.image(image, use_container_width=True)
    except:
        st.write("")

# Spacer
st.markdown("<br>", unsafe_allow_html=True)

# LIVEWIRE: Image Left, Text Right
livewire_col1, livewire_col2 = st.columns([2, 3])

with livewire_col1:
    try:
        image = Image.open("266A2910 (2).jpg")
        st.image(image, use_container_width=True)
    except:
        st.write("")

with livewire_col2:
    st.markdown("""
        <div style="padding: 30px 40px;">
            <h3 style="color: #A96DA3; font-weight: bold;">Livewire Dance Crew</h3>
            <p style="color: #F5F5F5; font-size: 16px;"><strong>Collegiate Dance Club of VNRVJIET, Hyderabad</strong></p>
            <p style="color: #F5F5F5; font-size: 16px;">
            As the lead organizer of Livewire Dance Crew, I managed a vibrant team of 40 dancers, coordinating practices, competitions, and live events that consistently secured top spots at collegiate festivals. 
                I was also responsible for financial planning—overseeing event budgets, costume logistics, and travel coordination. On the creative front, I edited audio tracks and managed our digital presence, significantly expanding our outreach and fostering a strong sense of identity within the campus arts community.
            </p>
        </div>
    """, unsafe_allow_html=True)
