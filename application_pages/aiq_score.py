
import streamlit as st
import plotly.graph_objects as go

def run_aiq_score():
    st.header("AI-Q Score")
    st.markdown("Track your progress and visualize how your AI-Q score improves as you complete courses.")

    # Example data (replace with actual data and calculations)
    courses = ["Python for Data Science", "Machine Learning Basics", "Advanced Data Analysis"]
    completed_courses = st.multiselect("Completed Courses", options=courses)

    # Example AI-Q score calculation based on completed courses
    initial_aiq_score = 50  # Example initial score
    score_increase_per_course = 10  # Example increase per course

    aiq_score = initial_aiq_score + len(completed_courses) * score_increase_per_course
    if aiq_score > 100:
        aiq_score = 100

    st.subheader("Your AI-Q Score")
    st.write(f"Your current AI-Q score is: {aiq_score}")

    # Create a gauge chart to visualize the AI-Q score
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = aiq_score,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "AI-Q Score", 'font': {'size': 24}},
        gauge = {
            'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "royalblue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 40], 'color': 'red'},
                {'range': [40, 70], 'color': 'yellow'},
                {'range': [70, 100], 'color': 'green'}],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
                'value': aiq_score}}))

    st.plotly_chart(fig, use_container_width=True)
