import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os
import git
from datetime import datetime

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

        # Set up Git repository details (replace with your actual GitHub repository details)
        REPO_DIR = "/path/to/your/local/repo"  # Local path to your cloned GitHub repo
        REPO_URL = "https://github.com/yourusername/yourrepo.git"  # Your GitHub repository URL
        BRANCH_NAME = "main"  # The branch to commit to (e.g., main or master)
        
        # Ensure that the repo is cloned locally
        if not os.path.exists(REPO_DIR):
            print("Cloning the repository...")
            git.Repo.clone_from(REPO_URL, REPO_DIR)
        
        # Create two columns for user input
        col1, col2 = st.columns(2)
        
        with col1:
            first_name = st.text_input("First Name:")
            middle_name = st.text_input("Middle Name:")
            last_name = st.text_input("Last Name:")
            id_number = st.text_input("ID Number")
            date_hired = st.date_input("Date Hired", value=None)
            civil_status = st.selectbox("Civil status:", ["Single", "Married", "Divorced", "Widowed"], index=None)
        
        with col2:
            birthdate = st.date_input("Birthdate", value=None)
            educational_attainment = st.selectbox(
                "Educational Attainment",
                ["N/A", "Doctorate", "Masters Graduate", "College Graduate", "K+12", "High School Graduate", "Elementary Graduate"],
                index=None
            )
            salary = st.number_input("Salary rate", min_value=0.0, step=100.0)
            wage_structure = st.selectbox("Wage Structure (daily/monthly)", ["Daily", "Monthly"], index=None)
        
        # Function to create "Employee Name" by combining last_name, first_name, and middle_name (middle initial)
        def create_employee_name(first_name, middle_name, last_name):
            middle_initial = middle_name[0] + '.' if middle_name else ''
            return f"{last_name}, {first_name} {middle_initial}"
        
        # Validate form data before submitting
        if st.button("Submit"):
            # Check if all required fields are filled
            if not first_name or not last_name or not id_number or not civil_status or not date_hired or not birthdate:
                st.error("Please fill in all required fields.")
            elif not salary or salary <= 0:
                st.error("Please enter a valid salary.")
            elif educational_attainment == "N/A":
                st.error("Please select a valid educational attainment.")
            else:
                # Create a DataFrame for the complete employee details
                complete_data = {
                    "First Name": [first_name],
                    "Middle Name": [middle_name],
                    "Last Name": [last_name],
                    "Birthdate": [birthdate],
                    "Date Hired": [date_hired],
                    "Civil Status": [civil_status],
                    "ID Number": [id_number],
                    "Salary Rate": [salary],
                    "Wage Structure": [wage_structure]
                }
        
                complete_df = pd.DataFrame(complete_data)
        
                # Define the file path to save the employee data (local file in the repository)
                complete_file_path = os.path.join(REPO_DIR, "employee_data.csv")
                
                # Save the data to a CSV file in the GitHub repo
                try:
                    if os.path.exists(complete_file_path):
                        existing_df = pd.read_csv(complete_file_path)
                        updated_df = pd.concat([existing_df, complete_df], ignore_index=True)
                        updated_df.to_csv(complete_file_path, index=False)
                    else:
                        complete_df.to_csv(complete_file_path, index=False)
                    
                    # Commit the changes to the local repo
                    repo = git.Repo(REPO_DIR)
                    repo.git.add(complete_file_path)
                    repo.index.commit(f"Add new employee entry {first_name} {last_name} on {datetime.now()}")
                    repo.remotes.origin.push()
        
                    st.success("Data successfully saved and pushed to GitHub!")
                except Exception as e:
                    st.error(f"An error occurred while saving to GitHub: {e}")
        
                
        






















































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
