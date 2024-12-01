import streamlit as st

# Custom CSS for styling
st.markdown("""
    <style>
    h1 {
        color: #D97757;
    }
    h2 {
        color: #6B7280;
    }
    .socials-link {
        color: #3498db;
        text-decoration: none;
    }
    .socials-link:hover {
        color: #2980b9;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("Follow Me On Social Media")

# Subheading
st.subheader("Connect with me on various platforms!")

# Social media links
st.markdown("""
Here are the links to my social media profiles and other platforms where I share my work:

- [GitHub](https://github.com/Sandesh13fr)  
- [LinkedIn](https://linkedin.com/in/sandesh13fr)    
- [Instagram](https://www.instagram.com/Sandesh13.0_jrdev)  
- [Codepen]("https://codepen.io/sandesh13fr")
- [Dottbio]("https://dott.bio/sandeshdawkhar13")

""", unsafe_allow_html=True)

# Optional: Add some social media icons (you can use any icon library like FontAwesome or external image links)
# st.markdown("""
#     # <div style="display: flex; justify-content: center; align-items: center;">
#     #     <a href="https://github.com/yourusername" target="_blank">
#     #         <img src="https://upload.wikimedia.org/wikipedia/commons/a/ab/LinkedIn_logo_initials.png" alt="GitHub" width="50" height="50">
#     #     </a>
#     #     <a href="https://www.linkedin.com/in/yourusername" target="_blank">
#     #         <img src="https://upload.wikimedia.org/wikipedia/commons/0/08/LinkedIn_logo_2013.svg" alt="LinkedIn" width="50" height="50">
#     #     </a>
#     #     <a href="https://www.instagram.com/yourusername" target="_blank">
#     #         <img src="https://upload.wikimedia.org/wikipedia/commons/9/95/Instagram_logo_2022.svg" alt="Instagram" width="50" height="50">
#     #     </a>
#     </div>
# """, unsafe_allow_html=True)

# Optional: Add a call to action or note
st.markdown("""
Feel free to reach out to me for collaborations, questions, or just to connect!  
Stay updated with my latest content by following me on these platforms.
""")
