🧠 AI Quiz Builder

-> An AI-powered Quiz Generator built using FastAPI, Streamlit, and Google Gemini API. It generates multiple-choice quizzes from a user-provided topic or uploaded PDF/TXT files and provides instant evaluation.

✨ Features
1.Generate quizzes from any topic
2.Generate quizzes from PDF and TXT files
3.Select difficulty (Easy, Medium, Hard)
4.Choose the number of questions
5.Automatic scoring and results
6.FastAPI backend with Streamlit frontend

🛠️ Tech Stack
> Python
> FastAPI
> Streamlit
> Google Gemini API
> PyPDF2
> Pydantic

📦 Installation
1. Clone the repository:
    > git clone: https://github.com/your-username/AI-Quiz-Builder.git
    > cd AI-Quiz-Builder

2. Create a virtual environment: python -m venv venv

Activate the virtual environment:
> Windows : venv\Scripts\activate
> Linux/macOS: source venv/bin/activate

3. Install dependencies: pip install -r requirements.txt

4. Create a .env file
    > GEMINI_API_KEY=your_gemini_api_key

▶️ Run the Project
> Start the FastAPI Backend: uvicorn main:app --reload
> Start the Streamlit Frontend (in a new terminal): streamlit run app.py

Open the Streamlit URL shown in the terminal (usually http://localhost:8501).

📁 Project Structure
AI-Quiz-Builder/
│── app.py
│── main.py
│── quiz_generator.py
│── models.py
│── config.py
│── requirements.txt
│── .env
└── README.md

🚀 Future Improvements
1.User authentication
2.Quiz history
3.Database integration
4.Export quiz as PDF
5.Support DOCX files


📄 License

This project is licensed under the MIT License.
