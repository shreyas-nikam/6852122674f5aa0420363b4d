id: 6852122674f5aa0420363b4d_documentation
summary: AI Risk Score - v2 Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# AI Risk Score Application Codelab

This codelab guides you through the AI Risk Score application, a Streamlit-based tool designed to assess and mitigate job displacement risk due to advancements in Artificial Intelligence. This application helps users understand their individual (Idiosyncratic) and occupational (Systematic) risks, identify skills to develop, and improve their overall AI-Q Score. By completing this codelab, you'll gain a comprehensive understanding of the application's structure, functionality, and how to extend it.

## Setting Up Your Environment
Duration: 00:05

Before diving into the code, ensure you have the following installed:

*   Python 3.7+
*   Streamlit
*   Pandas (for data handling, although not heavily used in this basic example)
*   Plotly (for the AI-Q score visualization)

You can install the necessary packages using pip:

```console
pip install streamlit pandas plotly
```

## Understanding the Application Structure
Duration: 00:10

The application is structured as follows:

*   `app.py`: This is the main entry point of the Streamlit application. It handles the overall layout, navigation, and imports the individual page functionalities.
*   `application_pages/`: This directory contains separate modules for each page of the application.
    *   `risk_assessment.py`:  Implements the risk assessment functionality.
    *   `aiq_score.py`: Implements the AI-Q score visualization.
    *   `learning_resources.py`: Provides links to relevant learning resources.

This modular design makes the application easier to maintain and extend.

## Exploring the `app.py` File
Duration: 00:15

The `app.py` file is the heart of the application. Let's break it down:

```python
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
```

Key components:

*   `st.set_page_config()`: Sets the page title and layout.  `layout="wide"` utilizes the full screen width.
*   `st.sidebar`: Adds a logo and a navigation menu to the sidebar.
*   `st.title()`: Sets the main title of the application.
*   `st.markdown()`: Displays descriptive text about the application.
*   `st.sidebar.selectbox()`: Creates a dropdown menu in the sidebar for navigating between different sections of the application.  The `options` list defines the pages.
*   `if/elif/else`:  This conditional block imports and executes the function associated with the selected page.  For example, if "Risk Assessment" is selected, it imports `run_risk_assessment` from `application_pages.risk_assessment` and calls it.
*   `st.divider()`: Adds a horizontal line to visually separate sections.
*   `st.write()` and `st.caption()`: Display copyright information and a disclaimer.

This `app.py` file effectively acts as a router, directing the user to the appropriate page based on their selection in the navigation menu.

## Examining the Risk Assessment Page (`risk_assessment.py`)
Duration: 00:20

This page allows users to input their occupation and skills to get a risk assessment.

```python
import streamlit as st
import pandas as pd

def run_risk_assessment():
    st.header("Risk Assessment")
    st.markdown("Enter your occupation and skills to assess your AI-related job displacement risk.")

    occupation = st.text_input("Occupation", "Data Scientist")
    skills = st.multiselect("Skills", options=["Python", "Machine Learning", "Data Analysis", "Communication", "Project Management"])

    if st.button("Assess Risk"):
        # Placeholder for risk assessment logic
        st.subheader("Risk Assessment Results")
        st.write(f"Occupation: {occupation}")
        st.write(f"Skills: {skills}")

        # Example calculations (replace with actual calculations based on the formulas)
        human_capital_factor = 0.7  # Example value
        company_risk_factor = 0.8  # Example value
        upskilling_factor = 0.9  # Example value

        idiosyncratic_risk = human_capital_factor * company_risk_factor * upskilling_factor
        systematic_risk = 0.6  # Example value

        st.write(f"Idiosyncratic Risk: {idiosyncratic_risk:.2f}")
        st.write(f"Systematic Risk: {systematic_risk:.2f}")

        # Display a simple risk level based on the calculated risks
        overall_risk = (idiosyncratic_risk + systematic_risk) / 2
        if overall_risk < 0.5:
            risk_level = "Low"
        elif overall_risk < 0.7:
            risk_level = "Moderate"
        else:
            risk_level = "High"

        st.write(f"Overall Risk Level: {risk_level}")

if __name__ == "__main__":
    run_risk_assessment()
```

Key elements:

*   `st.header()`: Sets the title of the page.
*   `st.markdown()`:  Provides a description of the page's functionality.
*   `st.text_input()`: Creates a text input field for the user to enter their occupation. The default value is "Data Scientist".
*   `st.multiselect()`: Creates a multiselect dropdown for the user to select their skills.
*   `st.button()`: Creates a button that triggers the risk assessment logic when clicked.
*   The `if st.button("Assess Risk"):` block executes only when the button is pressed.
*   The code currently includes **placeholder calculations** for `idiosyncratic_risk`, `systematic_risk`, and `overall_risk`.  **This is a critical area for improvement.**  The actual risk assessment logic should be implemented here, based on a defined methodology (e.g., based on O*NET data, skill relevance to AI, etc.).
*   A simple `if/elif/else` block determines the `risk_level` based on the calculated `overall_risk`.

<aside class="negative">
The risk calculation in this example is highly simplified and serves only as a placeholder.  A real-world application would require a more sophisticated model and data sources to accurately assess risk.
</aside>

## Analyzing the AI-Q Score Page (`aiq_score.py`)
Duration: 00:20

This page visualizes the user's AI-Q score using a gauge chart.

```python
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
```

Key components:

*   `st.multiselect()`: Allows the user to select completed courses.
*   The AI-Q score is calculated based on the number of completed courses.  This is a **simplified calculation** and should be replaced with a more comprehensive scoring system in a real application.
*   `plotly.graph_objects`:  Used to create an interactive gauge chart.
*   `go.Figure(go.Indicator(...))`:  Defines the structure and appearance of the gauge chart.  The `value` is set to the calculated `aiq_score`.
*   `st.plotly_chart()`: Displays the Plotly chart in the Streamlit application.  `use_container_width=True` ensures the chart fits the available width.

<aside class="positive">
The use of Plotly allows for interactive charts, enhancing the user experience. Users can hover over the chart to see more details.
</aside>

## Reviewing the Learning Resources Page (`learning_resources.py`)
Duration: 00:10

This page provides links to relevant learning resources.

```python
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
```

Key features:

*   A dictionary `resources` stores course names and their corresponding links. This is a placeholder and should be replaced with a dynamic list based on the user's identified skill gaps.
*   The code iterates through the `resources` dictionary and displays each course as a clickable link using Markdown formatting: `[course name](URL)`.
*   Additional learning platforms are listed using `st.write()`.

## Running the Application
Duration: 00:02

To run the application, navigate to the directory containing `app.py` in your terminal and execute:

```console
streamlit run app.py
```

This will open the application in your web browser.

## Enhancements and Future Development
Duration: 00:30

This application provides a basic framework for assessing AI-related job displacement risk.  Here are some potential enhancements:

1.  **Implement a Robust Risk Assessment Model:** Replace the placeholder calculations in `risk_assessment.py` with a data-driven model.  This could involve:
    *   Using O*NET data to assess the automation potential of different tasks within an occupation.
    *   Evaluating the relevance of user-provided skills to AI-related tasks.
    *   Incorporating industry-specific risk factors.
2.  **Personalized Learning Recommendations:**  Based on the risk assessment, provide tailored learning recommendations in the `learning_resources.py` page.  This would require identifying the user's skill gaps and suggesting courses or resources to address them.
3.  **Data Persistence:**  Implement a mechanism to store user data (occupation, skills, completed courses, AI-Q score) so that it persists across sessions.  This could involve using Streamlit's session state or connecting to a database.
4.  **Integration with External APIs:** Integrate with APIs to fetch real-time data on job market trends, emerging skills, and relevant learning resources.
5.  **Improved UI/UX:** Enhance the user interface and user experience with better visualizations, clearer explanations, and more intuitive navigation.
6.  **Expand AI-Q Score Calculation:** The current calculation is rudimentary. Incorporate factors like industry experience, adaptability, and continuous learning into the AI-Q score.
7. **Add User Authentication:** Implement user authentication to provide a more personalized experience and track individual progress over time.

<aside class="positive">
Consider using Streamlit's session state (`st.session_state`) for managing user data within a single session. This is a simple way to persist data without a database.
</aside>

<aside class="negative">
Be mindful of data privacy when collecting and storing user information. Ensure compliance with relevant regulations (e.g., GDPR).
</aside>

## Architecture Diagram
Duration: 00:05

```mermaid
graph LR
    A[User] --> B(Streamlit App - app.py);
    B --> C(Risk Assessment - risk_assessment.py);
    B --> D(AI-Q Score - aiq_score.py);
    B --> E(Learning Resources - learning_resources.py);
    C --> F{O*NET Data\n(Future)};
    D --> G{Plotly};
    E --> H(External Learning Platforms);
    style B fill:#f9f,stroke:#333,stroke-width:2px
```

This diagram illustrates the basic architecture of the application. The user interacts with the Streamlit application (`app.py`), which routes the request to the relevant modules. Future enhancements might include integrating with O*NET data for risk assessment and leveraging external learning platforms.

By working through this codelab, you've gained a solid understanding of the AI Risk Score application's structure, functionality, and potential for future development. This knowledge empowers you to extend and customize the application to meet specific needs and improve its overall effectiveness.
