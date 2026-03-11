import streamlit as st
import re

st.set_page_config(page_title="NivaraHealth")

# State variables
if "show_password" not in st.session_state:
    st.session_state.show_password = False

email = ""
password = ""
role = ""
remember_me = False
errors = {}

st.markdown("## NivaraHealth")
st.caption("Healthcare Management")

st.markdown("### Secure Login")
st.caption("Access your healthcare dashboard")

with st.form("login_form"):

    email = st.text_input(
        "Email Address",
        placeholder="doctor@nivarahealth.com"
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter your password"
    )

    role = st.selectbox(
        "Select Role",
        ["", "Administrator", "Doctor", "Staff", "Patient"]
    )

    remember_me = st.checkbox("Remember me")

    submitted = st.form_submit_button("Sign In Securely")

    if submitted:

        new_errors = {}

        if not email:
            new_errors["email"] = "Email is required"
        elif not re.match(r"\S+@\S+\.\S+", email):
            new_errors["email"] = "Please enter a valid email"

        if not password:
            new_errors["password"] = "Password is required"
        elif len(password) < 8:
            new_errors["password"] = "Password must be at least 8 characters"

        if not role:
            new_errors["role"] = "Please select your role"

        errors = new_errors

        if len(errors) == 0:
            st.write("Login attempt:", {
                "email": email,
                "role": role,
                "rememberMe": remember_me
            })

if "email" in errors:
    st.error(errors["email"])

if "password" in errors:
    st.error(errors["password"])

if "role" in errors:
    st.error(errors["role"])

st.markdown("[Forgot password?](#)")

st.markdown("---")

st.markdown("New to NivaraHealth?")

st.markdown("Don't have an account? **Request Access**")
