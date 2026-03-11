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

.left-box{
display:flex;
flex-direction:column;
justify-content:center;
align-items:center;
height:90vh;
color:white;
text-align:center;
}

.login-box{
background:white;
padding:40px;
border-radius:15px;
box-shadow:0 10px 30px rgba(0,0,0,0.2);
max-width:420px;
margin:auto;
}

.login-title{
text-align:center;
margin-bottom:20px;
}

.small-text{
color:#777;
font-size:14px;
text-align:center;
}

button[kind="primary"]{
background: linear-gradient(to right,#2F80ED,#27AE60);
border:none;
}

</style>
""", unsafe_allow_html=True)

left,right = st.columns([1.2,1])

with left:

    st.markdown('<div class="left-box">',unsafe_allow_html=True)

    st.image("https://cdn-icons-png.flaticon.com/512/3774/3774299.png",width=120)

    st.markdown("""
    <h1>Welcome to NivaraHealth</h1>
    <h4>Smart Healthcare, Simplified Management</h4>
    """,unsafe_allow_html=True)

    st.markdown('</div>',unsafe_allow_html=True)


with right:

    st.markdown('<div class="login-box">',unsafe_allow_html=True)

    st.markdown("""
    <div class="login-title">
    <h2>NivaraHealth</h2>
    <p class="small-text">Healthcare Management</p>
    </div>
    """,unsafe_allow_html=True)

    st.markdown("### Secure Login")

    email = st.text_input("Email Address",placeholder="doctor@nivarahealth.com")

    password = st.text_input("Password",type="password")

    role = st.selectbox("Select Role",
    ["Choose role","Administrator","Doctor","Staff","Patient"])

    remember = st.checkbox("Remember me")

    if st.button("Sign In Securely",type="primary"):

        errors=[]

        if not email:
            errors.append("Email required")

        elif not re.match(r'[^@]+@[^@]+\.[^@]+',email):
            errors.append("Invalid email")

        if not password:
            errors.append("Password required")

        if role=="Choose role":
            errors.append("Select role")

st.set_page_config(page_title="NivaraHealth", layout="wide")

# ---------- CSS ----------
st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
background: linear-gradient(135deg,#2F80ED,#27AE60);
}

.main{
padding-top:0rem;
}

.left-section{
height:100vh;
display:flex;
flex-direction:column;
justify-content:center;
align-items:center;
color:white;
text-align:center;
}

.left-section h1{
font-size:40px;
font-weight:700;
}

.left-section p{
font-size:20px;
opacity:0.9;
}

.login-card{
background:white;
padding:40px;
border-radius:20px;
box-shadow:0 15px 40px rgba(0,0,0,0.25);
max-width:420px;
margin:auto;
}

.logo-box{
display:flex;
align-items:center;
gap:10px;
justify-content:center;
margin-bottom:20px;
}

.logo-icon{
width:40px;
height:40px;
background:linear-gradient(135deg,#2F80ED,#27AE60);
border-radius:8px;
display:flex;
align-items:center;
justify-content:center;
color:white;
font-weight:bold;
}

.secure-title{
text-align:center;
margin-bottom:20px;
}

.secure-title h2{
margin:0;
}

button[kind="primary"]{
background: linear-gradient(to right,#2F80ED,#27AE60);
border:none;
}

</style>
""", unsafe_allow_html=True)

left,right = st.columns([1.2,1])

# ---------- LEFT SIDE ----------
with left:

    st.markdown('<div class="left-section">',unsafe_allow_html=True)

    st.image("https://cdn-icons-png.flaticon.com/512/3774/3774299.png",width=120)

    st.markdown("""
    <h1>Welcome to NivaraHealth</h1>
    <p>Smart Healthcare, Simplified Management</p>
    """,unsafe_allow_html=True)

    st.markdown("</div>",unsafe_allow_html=True)


# ---------- RIGHT SIDE ----------
with right:

    st.markdown('<div class="login-card">',unsafe_allow_html=True)

    st.markdown("""
    <div class="logo-box">
        <div class="logo-icon">+</div>
        <div>
            <h3 style="margin:0;">NivaraHealth</h3>
            <p style="font-size:12px;color:gray;margin:0;">Healthcare Management</p>
        </div>
    </div>
    """,unsafe_allow_html=True)

    st.markdown("""
    <div class="secure-title">
        <h2>Secure Login</h2>
        <p style="color:gray;">Access your healthcare dashboard</p>
    </div>
    """,unsafe_allow_html=True)

    email = st.text_input("Email Address",placeholder="doctor@nivarahealth.com")
    password = st.text_input("Password",type="password",placeholder="Enter your password")

    role = st.selectbox(
        "Select Role",
        ["Choose role","Administrator","Doctor","Staff","Patient"]
    )

    remember = st.checkbox("Remember me")

    if st.button("Sign In Securely",type="primary"):

        errors=[]

        if not email:
            errors.append("Email required")

        elif not re.match(r'[^@]+@[^@]+\.[^@]+',email):
            errors.append("Invalid email")

        if not password:
            errors.append("Password required")

        elif len(password)<8:
            errors.append("Password must be at least 8 characters")

        if role=="Choose role":
            errors.append("Please select role")

        if errors:
            for e in errors:
                st.error(e)
        else:
            st.success("Login successful")

    st.markdown("<br>",unsafe_allow_html=True)

    st.markdown(
        '<a href="#" style="font-size:14px;color:#2F80ED;">Forgot password?</a>',
        unsafe_allow_html=True
    )

    st.markdown("<hr>",unsafe_allow_html=True)

    st.markdown(
        '<p style="text-align:center;color:gray;">New to NivaraHealth?</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p style="text-align:center;">Don\'t have an account? <span style="color:#27AE60;font-weight:600;">Request Access</span></p>',
        unsafe_allow_html=True
    )

    st.markdown("</div>",unsafe_allow_html=True)
