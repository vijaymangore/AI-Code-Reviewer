import streamlit as st
import google.generativeai as ai
import os
secrete_key = open('key.txt')
key = secrete_key.read()
ai.configure(api_key=key)
# Make a note of it very important (You could use your API key by using following methods)
# Set up your API Key either in code or via an environment variable
# Option 1: Directly set the API key in the code (Replace 'YOUR_API_KEY' with your actual API key)
# Option 2: Alternatively, you can set the GOOGLE_API_KEY environment variable in your system or terminal
# Example to set environment variable manually (if you prefer not to hardcode the API key in the script):
# os.environ["GOOGLE_API_KEY"] = "YOUR_API_KEY"
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# Example usage of the API to list available models
try:
    # List available models from the Generative AI service
    available_models = ai.list_models()
    
    if not available_models:
        print("No models found.")
    else:
        # Iterate and print the available models
        for model in available_models:
            print(f"Model Name: {model.name}")
            
except Exception as e:
    print(f"Error occurred: {e}")

# Define the System Prompt for the AI Code Reviewer
sys_prompt = """You are an AI Code Reviewer. 
When given a piece of Python code, analyze it carefully to identify any bugs or errors.
Provide suggestions to fix them. Your response must follow this structured format:
1. provide a sub-heading "Bug Report" (bold). 2. In the "Bug Report" section, list all the identified bugs or errors in a clear, numbered format (e.g., 1, 2, 3).
3. Next, provide a sub-heading "Fixed Code" (bold). 4. Under "Fixed Code," rewrite the original code with all the identified issues fixed.

Always maintain proper formatting and clarity in your response and to the point only. Do explain 'how' and 'why'. Use this format only.
"""

# List available models (optional, just for debugging purposes)
available_models = ai.list_models()
for model in available_models:
    print(model.name)  # Display available models for debugging (you can remove this later)

# Define the Generative AI model
model = ai.GenerativeModel(
    model_name="models/gemini-1.5-flash",  # Use the correct model name
    system_instruction=sys_prompt,
)

# Streamlit App Layout
st.title("💬 An AI Code Reviewer")

# Input text area for user to paste Python code
user_prompt = st.text_area(
    "Enter your Python code here...",
    placeholder="Enter your code",
    height=68,
)

# Button to trigger the code review
btn_click = st.button("Generate")

# Process the input and display the response when the button is clicked
if btn_click:
    if user_prompt.strip() == "":
        st.error("Please enter some Python code for review.")
    else:
        try:
            # Generate content using the AI model
            response = model.generate_content(user_prompt)
            st.markdown("## Code Review")  # Display the "Code Review" heading
            st.markdown(response.text)  # Use Markdown to display the generated review
        except Exception as e:
            st.error(f"An error occurred: {e}")
