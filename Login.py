import streamlit as st



#LOGIN
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


#Accounts that can be logged im (Also edit the last part for the credentials)
# Define valid credentials
valid_username = "user"
valid_password = "password"
valid_username1 = "user2"
valid_password1 = "password2"

# If user is already logged in, show the slots
if st.session_state.logged_in:
    st.write("")






























































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
