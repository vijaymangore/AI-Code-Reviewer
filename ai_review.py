import streamlit as st
import google.generativeai as ai
import os
f=open(r"C:/Users/ADMIN/Innomatics/genai/keys/Generative AI.txt")
key=f.read()
print(key)
ai.configure(api_key= key)


# System prompt for the AI Code Reviewer
sys_prompt = """You are an AI Code Reviewer. 
When given a piece of Python code, analyze it carefully to identify any bugs or errors.
Provide suggestions to fix them. Your response must follow this structured format:
1. provide a sub-heading "Bug Report" (bold). 2. In the "Bug Report" section, list all the identified bugs or errors in a clear, numbered format (e.g., 1, 2, 3).
3. Next, provide a sub-heading "Fixed Code" (bold). 4. Under "Fixed Code," rewrite the original code with all the identified issues fixed.

Always maintain proper formatting and clarity in your response and to the point only.Do explain 'how' and 'why'. Use this format only.
"""

# List available models (optional, just for debugging purposes)
available_models = ai.list_models()
for model in available_models:
    print(model.name)

# Define the Generative AI model

    model = ai.GenerativeModel(
        model_name="models/gemini-1.5-flash",  
        system_instruction=sys_prompt,
    )

# Streamlit App Layout
st.title("💬 An AI Code Reviewer")

# Input text area for user to paste Python code
user_prompt = st.text_area(
    "Enter your Python code here...",
    placeholder="Enter your code",
    height= 68,
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
            st.markdown(response.text)  # Use Markdown for formatted response
        except Exception as e:
            st.error(f"An error occurred: {e}")








