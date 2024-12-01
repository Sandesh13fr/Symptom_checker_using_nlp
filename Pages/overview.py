import streamlit as st


st.title("ℹ️ About the Project")
st.divider()

st.markdown("""
This project focuses on creating anx **Symptom Checker Bot** designed to provide users with tailored guidance and support. 
Using advanced **Natural Language Processing (NLP)** techniques and **Logistic Regression**, the system extracts key information from user input to generate accurate and context-aware responses.

The user-friendly interface, built with **Streamlit**, ensures accessibility and ease of interaction, allowing users to describe their concerns and receive meaningful feedback.
""")

st.subheader("🔍 Project Breakdown:")

st.subheader("📊 Dataset:")
st.markdown("""
The dataset forms the backbone of this project, containing labeled data for training:
- **Intents**: The purpose of user input, such as:
  - Mental health queries
  - Symptom checking
  - General greetings
- **Entities**: Specific information extracted from input, like:
  - Symptoms (e.g., anxiety, headache)
  - Emotional states (e.g., stress, mood)
  - Contextual details (e.g., duration, frequency)
- **Text**: Raw user input, such as _"I feel anxious"_ or _"I have trouble sleeping."_
""")

st.subheader("💻 Streamlit Interface:")
st.markdown("""
The **Streamlit** interface enables seamless interaction between users and the AI model:
- A **text input box** for users to describe symptoms or mental health concerns.
- A **response area** where the AI provides insights:
  - For symptom checking: Possible causes and suggestions.
  - For mental health assistance: Supportive advice or resource links.
- Integrated with the trained NLP model for intelligent and real-time responses.
""")

st.subheader("✅ Conclusion:")
st.markdown("""
This project successfully combines **NLP** and **user-focused design** to build a **Symptom Checker Bot** that understands and responds to user input. 

### Key Achievements:
- Utilized NLP and Logistic Regression to interpret and process input effectively.
- Built an intuitive interface using Streamlit, making it accessible to non-technical users.
- Demonstrated the potential for future enhancements, such as:
  - Expanding the dataset with more diverse inputs.
  - Incorporating **deep learning models** for improved accuracy.
  - Adding multilingual support for broader accessibility.

This project is a step forward in leveraging NLP for improving mental health and well-being.
""")
