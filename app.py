import streamlit as st
st.html(
    '''
    <style>
    h1{
    color:Gray;
    }
    hr {
        border-color: green;
    }
    p,li{
        color:;
    }
    h3,h2{
        color:#D97757;
    }
    </style>
    '''
)

Home=st.Page(
    page="Pages/welcome.py",
    title="Home",
    icon="🏠"
)
Symptom_Checker=st.Page(
    page="Pages/symp.py",
    title="Symptom checker",
    icon="⁉️"
)
History=st.Page(
    page="Pages/history.py",
    title="History",
    icon="🕒"
)
About=st.Page(
    page="Pages/overview.py",
    title="About",
    icon="🧠"
)
Socials=st.Page(
    page="Pages/socials.py",
    title="Socials",
    icon="🌐"
)
st.sidebar.link_button("Buy me a coffee","https://buymeacoffee.com/sandesh13fr",icon="☕",)
pages=st.navigation([Home,Symptom_Checker,History,About,Socials])
pages.run()