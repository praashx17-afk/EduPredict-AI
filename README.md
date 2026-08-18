# 🎓 EduPredict AI

### Student Performance Prediction & Analytics System

EduPredict AI is a Python and Streamlit web application that analyzes student academic information and provides a performance score, performance category, academic insights, and personalized study guidance.

The application considers factors such as attendance, study hours, internal marks, assignment scores, previous exam scores, and class participation.

---

## 🚀 Features

- 🎓 Student Performance Prediction
- 📊 Academic Performance Score
- 📅 Attendance Analysis
- 📚 Study Hours Analysis
- 📝 Internal Marks Analysis
- 📋 Assignment Analysis
- 🎯 Previous Exam Score Analysis
- 🙋 Class Participation Analysis
- 📈 Interactive Academic Profile Chart
- 📊 Performance Dashboard
- 💡 Personalized Study Advisor
- 📥 CSV Report Download
- 🤖 Motivation & Study Guidance
- 🔒 No API Key Required
- 💻 Runs Locally

---

## 🧠 How It Works

EduPredict AI takes academic information from the user and calculates a weighted performance score.

The application considers:

```text
Attendance
Study Hours
Internal Marks
Assignment Score
Previous Exam Score
Class Participation
```

Based on the calculated score, the student is placed into one of four categories:

```text
🏆 Excellent
🟢 Good
🟡 Average
🔴 Needs Improvement
```

The application also provides personalized suggestions based on the student's inputs.

> **Note:** The current version uses a weighted scoring system rather than a trained Machine Learning model.

---

## 📊 Performance Analysis

The performance score is calculated using weighted academic factors:

| Factor | Weight |
|---|---:|
| Attendance | 18% |
| Study Hours | 17% |
| Internal Marks | 20% |
| Assignment Score | 15% |
| Previous Exam Score | 20% |
| Class Participation | 10% |

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application Logic |
| Streamlit | Web Interface |
| Pandas | Data Handling |
| Plotly | Interactive Visualization |

---

## 📁 Project Structure

```text
EduPredict-AI/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the Project

```bash
cd EduPredict-AI
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Environment

**Windows:**

```powershell
.venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the application with:

```bash
streamlit run app.py
```

The application will open automatically in your browser.

If it does not open automatically, visit:

```text
http://localhost:8501
```

---

## 📱 Application Sections

### 🏠 Predictor

Enter academic information and generate a performance prediction.

### 📊 Dashboard

View previous analyses, average performance, and download results as a CSV file.

### 💡 Study Advisor

Select an area you want to improve and receive practical study suggestions.

### ℹ️ About

View information about the project, technologies, and features.

---

## 🎯 Example

Example student information:

```text
Attendance: 90%
Study Hours: 5 hours/day
Internal Marks: 85%
Assignment Score: 88%
Previous Exam Score: 86%
Class Participation: 90%
```

The application processes these values and generates a performance category and overall performance score.

---

## 🔐 Privacy

EduPredict AI does not require an external AI API or API key.

The calculations are performed locally by the application, and the current version does not send student information to an external AI service.

---

## 🌟 Future Improvements

Possible future improvements include:

- 🧠 Integration of a trained Machine Learning model
- 📄 Student report generation
- 💾 Database integration
- 📈 Long-term performance tracking
- 👨‍🏫 Teacher dashboard
- 🏫 Multiple student management
- 📊 Larger real-world datasets
- 📱 Improved mobile experience

---

## ⚠️ Disclaimer

EduPredict AI is an educational project designed for academic analysis and learning purposes.

The generated performance categories are based on the scoring system implemented in the application and should **not** be considered an official academic evaluation.

---

## 👨‍💻 Author

**Utkarsh Singh**

B.Tech Computer Science  
Data Science

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

### 🎓 EduPredict AI

**Learn • Analyze • Improve • Grow 🚀**