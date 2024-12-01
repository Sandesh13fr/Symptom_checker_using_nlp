import streamlit as st


# st.title("🩺 Isayu AI Chatbot")

# Create two columns for layout
col1, col2 = st.columns([2, 1])
    
with col1:
    st.markdown("""
    ## Welcome to Your Personal Health Companion!
    
    _Isayu AI_ is here to assist you with:
    - Identifying potential health concerns
    - Offering symptom-based guidance
    - Providing wellness tips and recommendations
    
    ### How to Use
    1. Enter your symptoms in the chat box below.
    2. Receive potential insights based on your input.
    3. Explore suggestions to better understand your health.
    
    **Note:** 
    - This tool is not a replacement for professional medical advice.
    - Always consult a healthcare provider for serious or concerning symptoms.
    """)
    
with col2:
        # Optional: Add a health-related image or icon
        st.image("https://iili.io/20V9Kas.png", width=250)
    
    # Chat input
st.link_button("Start Chatting","https://symptom-checker-v1.streamlit.app/symp",icon="💬",type="primary",help="At your own risk")
