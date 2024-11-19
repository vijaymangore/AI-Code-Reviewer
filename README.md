# 💬 AI Code Reviewer
### An interactive Streamlit application powered by Google Generative AI to review Python code. This application identifies bugs, suggests fixes, and provides an improved version of the input Python code with structured and clear explanations.

## 🚀 Features
#### AI-Driven Code Review: Analyzes Python code for bugs and errors.
#### Structured Feedback: Provides a bug report and the corrected code following a clear, predefined format.
#### Interactive User Interface: Built with Streamlit for ease of use.
#### Powered by Google Generative AI: Utilizes the Gemini model for accurate code analysis.
## 🛠️ Requirements
#### Python 3.8 or higher
#### Required Python libraries:
#### streamlit
#### google.generativeai
#### Access to the Generative AI API with a valid API key.
## 🔧 Setup Instructions
#### Clone the repository:

#### bash
#### Copy code
#### git clone https://github.com/your-username/ai-code-reviewer.git
#### cd ai-code-reviewer
#### Install dependencies:

#### bash
#### Copy code
#### pip install -r requirements.txt
#### Set up API Key:

#### Place your Generative AI API key in a .txt file, e.g., Generative AI.txt.
#### Save the file in the specified directory (C:/Users/ADMIN/Innomatics/genai/keys/).
####  Run the application:

#### bash
#### Copy code
#### streamlit run app.py
## 🖥️ How to Use
#### Open the app in your browser (default: http://localhost:8501).
#### Enter your Python code in the text area provided.
 ####Click the Generate button to receive a detailed bug report and fixed code.
## ⚙️ Application Workflow
#### System Prompt: The AI is instructed to function as a code reviewer, delivering feedback in a structured format.
#### Model Setup: Uses the Gemini model from Google Generative AI.
#### Streamlit Interface:
#### Text area for Python code input.
#### Button to trigger AI review.
#### Error handling for empty inputs or API issues.
### Output:
#### Displays a formatted "Code Review" section with detailed feedback.
#### 📝 Example Output
#### Input:
#### python
#### Copy code
#### x = [1, 2, 3]
#### for i in x
   #### print(i)
#### Output:
#### Bug Report:
#### Missing colon : at the end of the for loop declaration.
#### Fixed Code:
#### python
#### Copy code
#### x = [1, 2, 3]
#### for i in x:
  #### print(i)
#### Explanation:
#### The syntax error occurred because the for loop declaration was missing a colon : at the end.

### 📜 License
#### This project is licensed under the MIT License. See the LICENSE file for details.

### 🙌 Acknowledgments
#### Streamlit: For enabling a seamless web app experience.
#### Google Generative AI: For providing state-of-the-art AI capabilities.
