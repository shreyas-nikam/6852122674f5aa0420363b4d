
import streamlit as st

def run_learning_resources():
    st.header("Learning Resources")
    st.markdown("Explore these learning resources to improve your skills and reduce your AI-related job displacement risk.")

    # Example learning resources (replace with actual resources based on skill gaps)
    resources = {
        "Python for Data Science": "https://www.example.com/python-data-science",
        "Machine Learning Basics": "https://www.example.com/machine-learning-basics",
        "Advanced Data Analysis": "https://www.example.com/advanced-data-analysis"
    }

    st.subheader("Recommended Courses")
    for course, link in resources.items():
        st.write(f"- [{course}]({link})")

    st.subheader("Other Resources")
    st.write("- QuantUniversity Courses: [https://www.quantuniversity.com/courses](https://www.quantuniversity.com/courses)")
    st.write("- Online Learning Platforms: Coursera, edX, Udacity")
