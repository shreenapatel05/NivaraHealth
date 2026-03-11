import streamlit as st
import re

st.set_page_config(page_title="NivaraHealth", layout="wide")

st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
background: linear-gradient(135deg,#2F80ED,#27AE60);
}

/* Right side background */
[data-testid="column"]:nth-child(2){
background:#F3F4F6;
height:100vh;
display:flex;
align-items:center;
justify-content:center;
}

/* Left content */
.left{
display:flex;
flex-direction:column;
justify-content:center;
align-items:center;
height:100vh;
color:white;
text-align:center;
}

.left h1{
font-size:44px;
font-weight:700;
}

.left p{
font-size:22px;
opacity:0.9;
}

/* Login Card */
.login-card{
background:white;
padding:40px;
border-radius:18px;
box-shadow:0 20px 40px rgba(0,0,0,0.15);
width:420px;
}

/* Logo */
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

/* Button */
button[kind="primary"]{
background:#0B5ED7 !important;
color:white !important;
font-weight:600;
border:none;
border-radius:8px;
width:100%;
}

button[kind="primary"]:hover{
background:#084298 !important;
}

/* Forgot password */
a{
color:#2F80ED !important;
text-decoration:none;
font-size:14px;
}

a:hover{
text-decoration:underline;
}

</style>
""", unsafe_allow_html=True)

left,right = st.columns([1.3,1])

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

    col1,col2 = st.columns([1,1])

    with col1:
        remember = st.checkbox("Remember me")

    with col2:
        st.markdown("<div style='text-align:right'><a href='#'>Forgot password?</a></div>", unsafe_allow_html=True)

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

    st.markdown("---")

    st.markdown("New to NivaraHealth?")

    st.markdown("Don't have an account? **Request Access**")

    st.markdown("</div>", unsafe_allow_html=True)
