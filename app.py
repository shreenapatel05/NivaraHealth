import streamlit as st
import re

st.set_page_config(page_title="NivaraHealth", layout="wide")

st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
background: linear-gradient(135deg,#2F80ED,#27AE60);
}

.main{
padding-top:0rem;
}

.container{
display:flex;
height:100vh;
}

.left{
flex:1;
display:flex;
flex-direction:column;
justify-content:center;
align-items:center;
color:white;
text-align:center;
}

.left h1{
font-size:42px;
font-weight:700;
}

.left p{
font-size:22px;
opacity:0.9;
}

.right{
flex:1;
display:flex;
justify-content:center;
align-items:center;
}

.login-card{
background:white;
padding:40px;
border-radius:20px;
box-shadow:0 10px 30px rgba(0,0,0,0.2);
width:420px;
}

.logo{
display:flex;
align-items:center;
gap:10px;
justify-content:center;
margin-bottom:20px;
}

.logo-box{
width:40px;
height:40px;
background:linear-gradient(135deg,#2F80ED,#27AE60);
border-radius:10px;
display:flex;
align-items:center;
justify-content:center;
color:white;
font-weight:bold;
}
button[kind="primary"]{
background:#0B5ED7 !important;
color:white !important;
font-weight:600;
border:none;
border-radius:8px;
}

button[kind="primary"]:hover{
background:#084298 !important;
color:white !important;
}
}

</style>
""", unsafe_allow_html=True)

left,right = st.columns([1.2,1])

# LEFT SIDE
with left:

    st.markdown('<div class="left">', unsafe_allow_html=True)

    st.image("https://cdn-icons-png.flaticon.com/512/3774/3774299.png", width=120)

    st.markdown("""
    <h1>Welcome to NivaraHealth</h1>
    <p>Smart Healthcare, Simplified Management</p>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


# RIGHT SIDE LOGIN
with right:

    st.markdown('<div class="login-card">', unsafe_allow_html=True)

    st.markdown("""
    <div class="logo">
        <div class="logo-box">+</div>
        <div>
            <h3 style="margin:0;">NivaraHealth</h3>
            <p style="font-size:12px;color:gray;margin:0;">Healthcare Management</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Secure Login")
    st.caption("Access your healthcare dashboard")

    email = st.text_input("Email Address", placeholder="doctor@nivarahealth.com")
    password = st.text_input("Password", type="password", placeholder="Enter your password")

    role = st.selectbox(
        "Select Role",
        ["Choose role","Administrator","Doctor","Staff","Patient"]
    )

    remember = st.checkbox("Remember me")

    if st.button("Sign In Securely", type="primary"):

        errors = []

        if not email:
            errors.append("Email required")

        elif not re.match(r"\S+@\S+\.\S+", email):
            errors.append("Invalid email")

        if not password:
            errors.append("Password required")

        elif len(password) < 8:
            errors.append("Password must be at least 8 characters")

        if role == "Choose role":
            errors.append("Please select role")

        if errors:
            for e in errors:
                st.error(e)
        else:
            st.success("Login successful")

    st.markdown("[Forgot password?](#)")

    st.markdown("---")

    st.markdown("New to NivaraHealth?")

    st.markdown("Don't have an account? **Request Access**")

    st.markdown("</div>", unsafe_allow_html=True)
