import streamlit as st
import requests

# Function to fetch a random joke from the API
def get_random_joke():
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")

        if response.status_code == 200:
            joke_data = response.json()
            return f"**{joke_data['setup']}** \n\n_{joke_data['punchline']}_"
        else:
            return "Failed to fetch a joke. Please try again later."
    except Exception as e:
        return f"Error: {str(e)}"

# Main function to run the Streamlit app
def main():
    st.set_page_config(page_title="Random Joke Generator", layout="wide", page_icon="🎉")

    # Custom CSS for styling (set body background to black)
    st.markdown(
        """
        <style>
       body {
        background-color: #000000; /* Black background */
        color: #ffffff; /* White text color */
    }
    .stButton {
        background-color: #ff6347; /* Tomato color */
        color: white;
        font-size: 16px;
        padding: 12px 30px;
        border-radius: 8px;
        border: 4px solid #ff4500; /* Colorful border for button */
    }
    .stButton:hover {
        background-color: #ff4500; /* Darker Tomato color */
        border: 4px solid #ff6347; /* Change border color on hover */
    }
    .joke-display {
        border: 4px solid #ff6347; /* Colorful border for joke display */
        border-radius: 8px;
        padding: 10px;
        margin-top: 20px;
        text-align: center; /* Center the text */
        font-size: 28px; /* Increased font size */
        font-weight: bold; /* Make text bold */
        color: #f39c12; /* Fun color for the text */
    }
    .stTextInput, .stSelectbox {
        background-color: #333333; 
        color: white;
        border-radius: 5px;
        padding: 10px;
        font-weight: bold;  /* Make input text bold */
        font-size: 38px;     /* Increase font size for better readability */
    }
    .stMarkdown {
        font-family: "Arial", sans-serif;
    }
       
    .footer {
        font-size: 24px;  /* Increased font size */
        color: #ccc;
        text-align: center;
        margin-top: 20px;
        font-weight: bold; /* Make the text bold */
    }
    .footer a {
        color: #ff6347; /* Tomato color for the link */
        font-size: 26px; /* Make the link text larger */
        font-weight: bold; /* Make the link text bold */
    }
    .divider {
        border: 2px solid #ff6347;
        margin: 20px 0;
    }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Title and description of the app
    st.title("🎉💥 Random Joke Generator 💥🎉")
    st.write("Click the button below to generate a random joke and brighten your day! 🤩")

    # Create button and handle click
    if st.button("Generate Joke 🤣"):
        # Get random joke when button clicked
        joke = get_random_joke()
        # Display joke with success styling
        st.markdown(f"<div class='joke-display'> {joke} </div>", unsafe_allow_html=True)

    # Divider for UI separation
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # Footer using HTML, displaying text in the center with an icon
    st.markdown(
        """
        <div class="footer">
            📝 Joke from Official Joke API<br>
            Built with ❤️💻 by <a href='https://github.com/codewithhoney' target='_blank' style="color: #ff6347; font-size: 28px;">Nousheen Atif</a> using Streamlit 🚀
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
