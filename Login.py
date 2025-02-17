import streamlit as st
from streamlit_option_menu import option_menu

# LOGIN
# Apply custom CSS to adjust the size of the text input fields
page_bg_img = f"""
<style>
.st-emotion-cache-1yiq2ps {{
    background-image: url("https://images.unsplash.com/photo-1735908235870-f4dd182a2f12?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D.jpg");        
    background-size: cover;
}}
.st-emotion-cache-h4xjwg {{
    background-color: rgba(0, 0, 0, 0);
}}
.st-emotion-cache-pb6fr7 {{
    width: 380px;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Initialize session state if it doesn't exist
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Accounts that can be logged in (Also edit the last part for the credentials)
# Define valid credentials
valid_username = "user"
valid_password = "password"
valid_username1 = "user2"
valid_password1 = "password2"

# If user is already logged in, show the slots
if st.session_state.logged_in:
    st.write("")

    with st.sidebar:
        app = option_menu(
            menu_title="HR Modules",  # Title of the menu
            options=["Employee Info Sheet", "Employee Profile", "Daily time record", "Payroll", "Mandatory Benefits Report", "Downloads"],  # Menu options
            icons=["house-fill", "people-fill", "clock", "calculator", "shield", "download"],  # Icons for each option
            styles={
                "container": {"padding": "5px", "background-color": "#f0f0f5"},
                "icon": {"color": "darkblue", "font-size": "16px"},
                "menu-title": {"font-size": "18px", "font-weight": "bold", "color": "darkblue"},
                "nav-link": {"font-size": "14px", "font-weight": "normal", "color": "darkblue"},
                "nav-link-selected": {"background-color": "#a0a0a0", "color": "white"},
            }
        )

    # This line should have no extra indentation!
    if app == "Employee Info Sheet":
        # Inject custom CSS for styling
        st.markdown("""
            <style>
                /* Style for text input fields */
                .stTextInput>div>div>input {
                    width: 500px !important;
                    height: 20px !important;
                    font-size: 16px !important;
                }

                /* Style for date input fields */
                input[type="date"] {
                    width: 380px !important;
                    height: 40px !important;
                    font-size: 16px !important;
                }

                /* Style for radio buttons */
                .stRadio>div>label {
                    font-size: 18px !important;
                }
            </style>
        """, unsafe_allow_html=True)

        st.title("Employee Information Sheet")
























































#LOGIN continuation
else:
    # Show login form if not logged in
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == valid_username and password == valid_password:
            # If the first username and password match
            st.session_state.logged_in = True
            st.success("***Kindly press login to continue!!!***")
        elif username == valid_username1 and password == valid_password1:
            # If the second username and password match
            st.session_state.logged_in = True
            st.success("***Kindly press login to continue!!!***")
        else:
            st.error("Invalid username or password!")
