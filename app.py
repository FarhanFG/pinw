import streamlit as st
import subprocess

# Title of the app
st.title("WhatsApp Access Keys")

# Input field for the PIN
pin = st.text_input("Enter PIN", type="password")

# Button to verify the PIN
if st.button("Submit"):
    if pin == "3434":
        try:
            # Execute the curl command
            response = subprocess.run(
                [
                    "curl", "-X", "GET", 
                    "http://13.126.242.31:8000/add-passcode", 
                    "-H", "accept: application/json"
                ],
                capture_output=True, text=True
            )
            
            # Display the output
            st.success("Request executed successfully!")
            st.code(response.stdout)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Invalid PIN. Please try again.")
