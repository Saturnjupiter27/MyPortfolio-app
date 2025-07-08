import streamlit as st
from PIL import Image
import base64

# --- CONFIG ---
st.set_page_config(page_title="Karna Mehta Portfolio", page_icon="💼", layout="wide")

# --- SET BACKGROUND ---
# --- HERO HEADER with IMAGE (only top section) ---
# --- HERO IMAGE HEADER ---
def hero_header(image_path):
    import base64
    with open(image_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(f"""
        <style>
        .hero-container {{
            width: 100%;
            overflow-x: hidden;
        }}
        .hero-img {{
            max-width: 100%;
            height: auto;
            display: block;
            margin: 0 auto;
        }}
        .hero-text {{
            text-align: left;
            margin-top: 1rem;
            padding-left: 2rem;
        }}
        </style>
        <div class="hero-container">
            <img class="hero-img" src="data:image/jpg;base64,{encoded}" alt="Karna Mehta Banner"/>
        </div>
        <div class="hero-text">
            <h1>Karna Mehta</h1>
            <p><strong>MS in Computer Science @ USC | AI/ML Researcher | Data Science Enthusiast | Web Developer | Educator</strong></p>
        </div>
    """, unsafe_allow_html=True)





hero_header("assets/KARNA_PROFILE_BACKGROUND.jpg")


# --- LOAD ASSETS ---
resume_file = "assets/Karna_Resume_2 (1).pdf"

# --- HERO SECTION ---
col1, col2 = st.columns([1, 3])



# --- NAVIGATION ---
st.markdown("## 🧭 Navigation")
pages = ["About", "Skills", "Projects", "Co-Curricular", "Contact"]
page = st.selectbox("Go to", pages)

# --- ABOUT SECTION ---
if page == "About":
    st.markdown("<h3 style='font-size: 28px;'>🧠 Overview</h3>", unsafe_allow_html=True)

    st.write("""
    I am a passionate Computer Science graduate student at the University of Southern California, with strong interests in Machine Learning, AI Chatbots, and Computer Vision. With a proven track record in research, full-stack development, and instructional roles, I bring a blend of technical expertise and leadership in AI-driven projects, backend systems, and educational platforms.
    """)

    st.markdown("<h3 style='font-size: 28px;'>👨‍🎓 Education</h3>", unsafe_allow_html=True)

    st.write("""
    - **MS in Computer Science**, USC (2025-Present) — GPA: 3.5/4.0  
    - **BTech in IT**, DJ Sanghvi College of Engineering (2021–2025) — GPA: 9.14/10
    """)

    st.markdown("<h3 style='font-size: 28px;'>💼 Work Experience</h3>", unsafe_allow_html=True)

    st.write("""
    - **ML Engineer Intern** at Shiga Corp (2023): AI manager chatbot, Transaction fraud Analysis, Credit Risk Prediction with Explainable AI  
    - **Python Dev & Instructor** at Brainlox (2022): Backend in Flask + teaching school students
    """)

# --- SKILLS SECTION ---
elif page == "Skills":
    st.markdown("### 🛠️ Technical Skills")
    cols = st.columns(4)
    skills = {
        "Programming": ["C", "C++", "Python", "JavaScript"],
        "Frameworks": ["Flask", "Django", "ReactJS", "Angular"],
        "AI/ML": ["NLP", "Computer Vision", "YOLOv8", "Machine Learning", "Generative AI"],
        "Tools": ["MongoDB", "MySQL", "PowerBI"]
    }
    for col, (cat, items) in zip(cols, skills.items()):
        col.markdown(f"**{cat}**")
        for item in items:
            col.write(f"- {item}")

# --- PROJECTS SECTION ---
elif page == "Projects":
    st.markdown("## 🚀 Notable Projects")
    st.markdown("---")

    def show_project(title, bullet_points):
        st.markdown(f"### 🔹 {title}")
        for point in bullet_points:
            st.markdown(f"- {point}")
        st.markdown("---")

    show_project("Q&A Chatbot for a Tourist in an Unknown City", [
        "Developed a conversational chatbot to assist tourists with navigation, local info, and common queries.",
        "Implemented NLP pipelines using tokenization, intent classification, and slot filling.",
        "Built and trained transformer-based models using PyTorch.",
        "Integrated fallback intents and multilingual support for real-world robustness."
    ])

    show_project("Artist Discovery Portal with Artsy API", [
        "Developed a full-stack web application allowing users to search, view, and favorite artists using the Artsy API.",
        "Implemented authentication with JWT, MongoDB Atlas for favorites, and protected routes for personalized access.",
        "Built dynamic search, artist detail pages with tabs (artworks, biography, similar artists), and category dialogs.",
        "Frontend: Angular with Tailwind; Backend: Node.js/Express; Deployed on Google Cloud with secure JWT cookies.",
        "[🌐 Live Demo](https://web-assignemnt3-karna.uw.r.appspot.com)"
    ])

    show_project("Quality Inspection System for Metal and Pills Defect Detection", [
        "Designed a two-part quality assurance system for industrial defect detection.",
        "Used morphological operations for metal surface defect segmentation.",
        "Implemented YOLOv8-based object detection for pill defect classification.",
        "Achieved high precision and recall; results published in **IMAVIS Journal**.",
        "[📄 View Research Paper](https://docs.google.com/document/d/1JpyvVPUekgFxCIMr2WF48OZ5HrUrRjyogEvEXiSDBnM/edit?usp=sharing)"
    ])

    show_project("Online Math Tutoring System for Teaching ‘Area Under the Curve’", [
        "Built a full-stack MERN web platform to visually teach definite integrals.",
        "Used scaffolding pedagogy to progressively reveal problem-solving steps.",
        "Enabled interactive graphs and real-time feedback for students.",
        "Research paper presented at **ICACIT Conference**.",
        "[📄 View Research Paper](https://docs.google.com/document/d/12HMrpgaendYLGy97p-MGzMgc2efUy_qkXIIitsal-FE/edit?usp=sharing)"
    ])

    show_project("Early Detection and Diagnosis of Brain-Related Diseases", [
        "Developed a multimodal diagnostic tool using voice biomarkers and MRI scans.",
        "Used Parselmouth-Praat to extract prosodic features from speech data.",
        "Applied DenseNet CNN architecture on MRI images for classification.",
        "Achieved significant early detection accuracy; presented at **ICICBDA Conference**.",
        "[📄 View Research Paper](https://docs.google.com/document/d/1Fx0nrQi7XPJwa7AcL8Vhzzr7oLzv4hM8HEp7pAoqnRk/edit?usp=sharing)"
    ])

    show_project("Health Record Portal for Predictive Diagnostics", [
        "Created a secure web-based health record system with predictive diagnostics.",
        "Users input symptoms; ML models predict disease probabilities.",
        "Recommendations are generated for preventive actions and follow-up.",
        "Used logistic regression, decision trees, and SVM models for backend predictions."
    ])

    show_project("Handwritten Text Recognition and Grammar Correction", [
        "Developed a pipeline to extract and clean handwritten text from scanned notes.",
        "Used OpenCV for image preprocessing and OCR (Tesseract) for text extraction.",
        "Applied spaCy-based NLP techniques for grammar detection and correction.",
        "Optimized for scanned student papers and whiteboard screenshots.",
        "**Published in IC-CCDS 2025**",
        "[📄 View Research Paper](https://docs.google.com/document/d/17p7Zl-ptv-VKiRTQwz29VgujpZpIGH-r/edit?usp=sharing&ouid=104285998543924643887&rtpof=true&sd=true)"
    ])

    show_project("Flower and Plant Species Identification", [
        "Trained a CNN classifier on a dataset of 6600 flower and plant images.",
        "Preprocessed images using data augmentation and color normalization.",
        "Achieved over 90% accuracy using a ResNet-based model.",
        "Built a Streamlit UI for interactive species prediction."
    ])

# --- CO-CURRICULAR SECTION ---
elif page == "Co-Curricular":
    st.markdown("## 🌟 Co-Curricular, Leadership & Volunteering")

    st.markdown("### 🏫 Co-Curricular Activities")
    st.write("""
    - **DJS-LIT (Official Literary Society of DJSCE)** *(Jul 2022 – Jun 2023)*  
      Served as the **Logistics Head**, managing events and operational duties.

    - **DJInIT.AI (AI/ML Club of DJSCE)** *(Sep 2022 – Jul 2023)*  
      Acted as **Junior Mentor**, guiding AI/ML projects, conducting workshops and hands-on sessions.

    - **DJInIT.AI (AI/ML Club of DJSCE)** *(Aug 2023 – Jun 2024)*  
      Held position of **Vice-President**: Led collaborative projects, hosted events, and supervised the club roadmap.

    - **Class Representative**  
      Represented classmates during Bachelor's, resolving academic and administrative issues.
    """)

    st.markdown("### 🙋‍♂️ Leadership Roles")
    st.write("""
    - **Class Representative & Head of Library Services** *(Jun 2022 – Feb 2024)*  
      Advocated for students' needs and coordinated library logistics for academic material access.

    - **Project Team Lead** *(Oct 2022 – May 2024)*  
      Led a 5-member development team through multiple AI/ML research and engineering projects.
    """)

    st.markdown("### ❤️ Volunteering Activities")
    st.write("""
    - **Grain-a-thon 2.0 – DJS NSS**  
      Collected and distributed grain donations to the homeless foundation.

    - **Blood Donation Camp – DJS NSS**  
      Assisted with donor coordination and operations, ensuring smooth blood collection and distribution.
    """)

# --- CONTACT SECTION ---
elif page == "Contact":
    st.markdown("### 📬 Contact Me")
    st.write("📧 Email: karnamehta8@gmail.com | karnajug@usc.edu")
    st.write("📞 Phone: +1 (213) 238-3488")
    st.write("[LinkedIn](https://www.linkedin.com/in/karna-mehta-2308b1219/)")

    st.markdown("### 💬 Leave a Message (simulation)")
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    if st.button("Send"):
        st.success("Thank you! Your message has been recorded.")
