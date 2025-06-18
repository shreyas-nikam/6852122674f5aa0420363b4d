
import streamlit as st

st.set_page_config(page_title="AI Risk Score - v2", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("AI Risk Score - v2")
st.divider()

st.markdown("""
In this lab, we explore the AI Risk Score, a tool to help you understand and mitigate your risk of job displacement due to advancements in Artificial Intelligence.
This application uses the concepts and formulas described in the research document to assess your individual risk (Idiosyncratic Risk) and the broader risk associated with your occupation (Systematic Risk).  By understanding these risks, you can identify skills to develop and improve your overall AI-Q Score, ultimately increasing your job security.
""")

# Your code starts here
page = st.sidebar.selectbox(label="Navigation", options=["Risk Assessment", "AI-Q Score", "Learning Resources"])

if page == "Risk Assessment":
    from application_pages.risk_assessment import run_risk_assessment
    run_risk_assessment()
elif page == "AI-Q Score":
    from application_pages.aiq_score import run_aiq_score
    run_aiq_score()
elif page == "Learning Resources":
    from application_pages.learning_resources import run_learning_resources
    run_learning_resources()
# Your code ends

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity.")
