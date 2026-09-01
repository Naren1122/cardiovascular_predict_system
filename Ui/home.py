import os
import sys
import streamlit as st

# Ensure UI directory is in sys.path so sub-pages can import models.py on Streamlit Cloud
_UI_DIR = os.path.dirname(os.path.abspath(__file__))
if _UI_DIR not in sys.path:
    sys.path.insert(0, _UI_DIR)

def home():
    # Header Banner
    st.markdown("""
    <div style="background: linear-gradient(135deg, #1E1E2E 0%, #2D1B36 100%); 
                padding: 25px 30px; 
                border-radius: 14px; 
                border-left: 6px solid #FF4B4B; 
                margin-bottom: 25px;">
        <h1 style="color: #FF4B4B; margin: 0; font-size: 2rem;">🫀 Cardiovascular Disease (CVD)</h1>
        <p style="color: #E0E0E0; font-size: 1.05rem; margin-top: 8px; margin-bottom: 0;">
            Understanding heart health, primary risk factors, and modern predictive diagnosis.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # What is CVD Section
    st.subheader("What is Cardiovascular Disease?")
    st.write(
        "Cardiovascular disease (CVD) is a general term for conditions affecting the heart or blood vessels. "
        "It is one of the leading causes of death worldwide, but many forms of CVD can be prevented or managed "
        "with healthy lifestyle choices and early risk detection."
    )

    st.write("")

    # Key Risk Factors & Common Symptoms in 2 Columns
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### ⚠️ Key Risk Factors
        - **High Blood Pressure (Hypertension):** Puts extra strain on blood vessels and heart.
        - **High Cholesterol & Glucose:** Can lead to fatty deposits (plaques) in arteries.
        - **Smoking & Alcohol:** Damages artery linings and raises heart attack risk.
        - **Physical Inactivity & Obesity:** Contributes to high BP and metabolic syndrome.
        - **Age & Genetics:** Risk naturally increases with age and family history.
        """)

    with col2:
        st.markdown("""
        ### 🚨 Common Warning Signs
        - Chest pain, tightness, pressure, or discomfort (Angina)
        - Shortness of breath during exertion or at rest
        - Pain, numbness, or weakness in legs or arms
        - Fluttering, rapid, or irregular heartbeat (Palpitations)
        - Persistent fatigue, dizziness, or lightheadedness
        """)

    st.write("---")

    # Prevention & Healthy Habits
    st.subheader("🛡️ Prevention & Heart-Healthy Habits")
    
    p1, p2, p3 = st.columns(3)
    with p1:
        st.info("**🥗 Balanced Nutrition**\n\nEat a diet rich in fruits, vegetables, whole grains, and lean proteins while lowering salt and saturated fats.")
    with p2:
        st.success("**🏃 Regular Exercise**\n\nAim for at least 150 minutes of moderate aerobic activity (e.g., brisk walking) per week.")
    with p3:
        st.warning("**🩺 Regular Checkups**\n\nMonitor blood pressure, blood glucose, and cholesterol levels periodically for early detection.")

    st.write("---")
    st.caption("Use the sidebar menu to navigate to the **Logistic Regression** and **SVM** prediction models.")


# Flat list navigation removes the nested category dropdowns
pages = [
    st.Page(home, title="Home", icon="🏠", default=True),
    st.Page('logistic.py', title='CardioVascular - Logistic', icon="📈"),
    st.Page('svm.py', title='CardioVascular - SVM', icon="⚡")
]

pg = st.navigation(pages)
pg.run()