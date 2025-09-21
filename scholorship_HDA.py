from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st   

import os
import streamlit as st

st.markdown(
    """
    <style>
    /* Style all selectboxes */
    div[role="combobox"] select {
        background-color: #ADD8E6 !important;  /* Light blue background */
        border: 2px solid #7DCEA0 !important;  /* Soft green border */
        border-radius: 8px !important;
        padding: 6px !important;
        color: #1C2833 !important;             /* Dark gray text */
        font-weight: bold !important;
        font-size: 16px !important;
    }

    /* Style buttons */
    .stButton>button {
        background-color: #FFB347;
        color: #ffffff;
        border-radius: 8px;
        padding: 8px 16px;
        font-weight: bold;
        border: none;
    }

    .stButton>button:hover {
        background-color: #FFDAB9;
        color: #4A4A4A;
    }
    </style>
    """,
    unsafe_allow_html=True
)

    



load_dotenv()


model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
)
st.title(" 🎓 SHOLORSHIP HUNTER")
st.write("🎯 Find scholarships that match your profile and aspirations.Please note that it is focused only on non-medical scholarships 🌏 ")
name=st.text_input("Enter your Full Name")
email=st.text_input("Enter your Email Address")

#SCHOLORSHIP TYPE
scholarship_type = st.selectbox(
    "Preferred Scholarship Type",
    ["Fully Funded", "Partially Funded", "Any / No Preference"]
)

#FIELD OF STUDY
field_of_study=st.selectbox("Select your Field of Study", ["Computer Science", "Business", "Engineering", "Arts", "Science", "Other"])
if field_of_study == "Engineering":
    engineering_field = st.selectbox(
        "Select your Engineering specialization", 
        [
            "Software Engineering",
            "Computer Engineering",
            "Electrical Engineering",
            "Mechanical Engineering",
            "Civil Engineering",
            "Biomedical Engineering",
            "Chemical Engineering",
            "Environmental Engineering",
            "Aerospace Engineering"
        ]
    )
    st.write("You selected:", engineering_field)
else:
    st.write("You selected:", field_of_study)
    if field_of_study == "Computer Science":
        cs_specialization = st.selectbox(
            "Select your Computer Science specialization", 
            [
                "Artificial Intelligence",
                "Data Science",
                "Cybersecurity",
                "Software Development",
                "Network Engineering",
                "Human-Computer Interaction",
                "Database Management",
                "Cloud Computing" 
            ]
        )
        st.write("You selected:", cs_specialization)
        
        #COUNTRY
country=st.text_input("Enter your Country of Residence")
primary_nationality = st.selectbox(
    "Select your primary nationality:",
    ["Pakistani", "Canadian", "American", "British", "Australian", "Other"]
)

secondary_nationality = st.selectbox(
    "Select your secondary nationality (if any):",
    ["None", "Pakistani", "Canadian", "American", "British", "Australian", "Other"]
)
nationalities = [primary_nationality]
if secondary_nationality != "None" and secondary_nationality != primary_nationality:
    nationalities.append(secondary_nationality)

#APPLYING FOR:
academic_level = st.selectbox(
    "Select your Academic Level",
    ["Undergraduate", "Graduate (Masters)", "PhD", "Certifications / Other"]
)

if academic_level == "Undergraduate":
    study_plan = st.selectbox(
        "Select your Study Plan",
        [
            "Full Degree Program",
            "Exchange Program (1-2 semesters abroad)",
            "Final Year or Last Semesters Abroad",
            "Short Courses / Certifications"
        ]
    )

elif academic_level == "Graduate (Masters)":
    study_plan = st.selectbox(
        "Select your Study Plan",
        [
            "Full Degree Program",
            "Exchange Program (1-2 semesters abroad)",
            "Final Year or Last Semesters Abroad",
            "Short Courses / Certifications"
        ]
    )

elif academic_level == "PhD":
    study_plan = st.selectbox(
        "Select your Study Plan",
        [
            "Full Degree Program",
            "Exchange Program (Research/Visiting)",
            "Short Courses / Summer Schools"
        ]
    )

else:
    study_plan = st.selectbox(
        "Select your Study Plan",
        [
            "Professional Certifications",
            "Short Courses",
            "Other Specialized Programs"
        ]
    )
st.write("You selected:", study_plan)
gpa=st.number_input("Enter your GPA (on a 4.0 scale)", min_value=0.0, max_value=4.0, step=0.01)
financial_need=st.selectbox("Do you have financial need?", ["Yes", "No"])
extracurriculars=st.text_area("List your Extracurricular Activities (comma separated)")
achievements=st.text_area("List your Notable Achievements (comma separated)")

promt=f"""
You are a scholarship advisor.
You must follow the instructions carefully and stay within your expertise.
If any information is missing or unclear, politely state the limitation instead of making up facts.

The user details are given below:   
USER PROFILE:
Name: {name}
Email: {email}
Preferred Scholarship Type: {scholarship_type}  
Field of Study: {field_of_study}
Country of Residence: {country}
Nationalities: {nationalities}  
Academic Level: {academic_level}
GPA: {gpa}
Financial Need: {financial_need}
Extracurricular Activities: {extracurriculars}
Notable Achievements: {achievements}

Based on this, provide:
1. A list of scholarships that best match the user's profile, considering:
   - Academic level
   - Field of study
   - Nationality (all listed nationalities)
   - Country of residence
   - Financial need
   - GPA
   - Extracurricular activities and achievements
2. Include the scholarship name, amount, eligibility requirements, and a brief description.
3. Cover scholarships from all around the world that are relevant to the user's profile.
4. If a scholarship is restricted to a specific country, note that clearly.
5. Present the list in a clear, concise, and organized manner.
6. Present links to official scholarship pages, if available.
7. Make the list sorted by "application deadline" or "amount" for easier use.

IMPORTANT RULES:
- Only provide scholarships that match the user's profile and eligibility.
- Do not suggest scholarships for which the user does not qualify.
- If the request is unrelated to scholarships, respond: "This app only supports scholarship recommendations."
- Keep the answer clear, step-by-step, and concise.
- Do not hallucinate or make up scholarship names, amounts, or details.
"""

if st.button("Find Scholarships"):
    with st.spinner("Finding Scholarships..."):
        result = model.invoke(promt)
        st.subheader("Recommended Scholarships")
        st.write(result.content)
