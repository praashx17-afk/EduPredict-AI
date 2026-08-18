import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import random

st.set_page_config(
    page_title="EduPredict AI",
    page_icon="🎓",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

*{font-family:Inter,sans-serif}
.stApp{
    background:
    radial-gradient(circle at 90% 5%,#eef2ff,transparent 25%),
    radial-gradient(circle at 10% 80%,#f0f9ff,transparent 25%),
    #fff
}
.block-container{max-width:1450px;padding:2rem 1rem 3rem}
#MainMenu,header,footer{visibility:hidden}

section[data-testid="stSidebar"]{
    background:linear-gradient(180deg,#f8faff,#eef2f9);
    border-right:1px solid #dfe5ef
}
section[data-testid="stSidebar"]>div{padding:1.5rem 1rem}

section[data-testid="stSidebar"] div[role="radiogroup"] label{
    background:#ffffffaa;
    border:1px solid #e2e8f0;
    border-radius:14px;
    padding:10px 12px;
    margin:4px 0;
    transition:.2s
}
section[data-testid="stSidebar"] div[role="radiogroup"] label:hover,
section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked){
    transform:translateX(4px);
    border-color:#a5b4fc;
    box-shadow:0 8px 20px #4f46e51a
}
section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked){
    background:linear-gradient(135deg,#eef2ff,#e0f2fe)
}

h1,h2,h3{color:#111827!important;font-weight:800!important}
p{color:#64748b}

.hero-badge{
    display:inline-block;
    background:#eef2ff;
    color:#4f46e5;
    border:1px solid #c7d2fe;
    padding:8px 15px;
    border-radius:50px;
    font-size:13px;
    font-weight:800
}
.hero-title{
    font-size:48px;
    font-weight:800;
    color:#111827
}
.hero-subtitle{
    font-size:18px;
    color:#64748b;
    line-height:1.7
}

div[data-testid="stMetric"]{
    background:linear-gradient(145deg,#fff,#f6f8ff);
    border:1px solid #e4e9f2;
    border-radius:20px;
    padding:20px;
    box-shadow:0 12px 28px #0f172a12;
    transition:.2s
}
div[data-testid="stMetric"]:hover{
    transform:translateY(-5px);
    box-shadow:0 20px 35px #0f172a1c
}

.stButton>button{
    width:100%;
    min-height:54px;
    border:0;
    border-radius:15px;
    background:linear-gradient(135deg,#4f46e5,#6366f1);
    color:#fff!important;
    font-weight:800;
    box-shadow:0 10px 25px #4f46e544
}
.stButton>button:hover{
    transform:translateY(-2px);
    background:linear-gradient(135deg,#4338ca,#4f46e5)
}
.stButton>button p{color:#fff!important}

.jarvis-card{
    display:block;
    text-decoration:none!important;
    background:linear-gradient(145deg,#fff,#eef2ff);
    border:1px solid #dbe3f0;
    border-radius:18px;
    padding:18px 10px;
    box-shadow:0 10px 25px #0f172a12;
    transition:.2s
}
.jarvis-card:hover{
    transform:translateY(-4px);
    border-color:#a5b4fc
}
.jarvis-icon{text-align:center;font-size:40px}
.jarvis-title{text-align:center;color:#111827!important;font-size:17px;font-weight:800}
.jarvis-subtitle{text-align:center;color:#64748b!important;font-size:11px;margin-top:5px}

.quote-box{
    background:linear-gradient(135deg,#eef2ff,#f0f9ff);
    border:1px solid #dbe4ff;
    border-radius:22px;
    padding:25px;
    margin:20px 0
}

.footer{text-align:center;color:#94a3b8;padding:25px 0;font-size:13px}
</style>
""", unsafe_allow_html=True)


QUOTES = [
    "Success is built one consistent effort at a time.",
    "Your future is created by what you do today.",
    "Small progress every day leads to big results.",
    "Every expert was once a beginner.",
    "Discipline will take you places motivation cannot.",
    "Keep learning. Keep improving. Keep moving forward.",
    "Your effort today is an investment in your future.",
    "Mistakes are not failure. They are part of learning.",
    "Consistency beats intensity in the long run.",
    "Believe in your progress and keep going."
]


if "history" not in st.session_state:
    st.session_state.history = []


def get_quote():
    return random.choice(QUOTES)


with st.sidebar:
    st.markdown("# 🎓 EduPredict AI")
    st.caption("Student Performance Intelligence")
    st.divider()

    page = st.radio(
        "Navigation",
        ["🏠 Predictor", "📊 Dashboard", "💡 Study Advisor", "ℹ️ About"],
        label_visibility="collapsed"
    )

    st.divider()
    st.markdown("### ⚡ System Status")
    st.success("🟢 Performance Engine Online")
    st.caption("Fast & Private")
    st.caption("No external API required")

    st.divider()
    st.markdown("### 🤖 Your AI Assistant")
    st.caption("Need help with something else?")

    st.markdown("""
<a href="https://chatgpt.com/" target="_blank" class="jarvis-card">
<div class="jarvis-icon">🤖</div>
<div class="jarvis-title">JARVIS</div>
<div class="jarvis-subtitle">Your AI Assistant</div>
<div class="jarvis-subtitle">Click to open ChatGPT →</div>
</a>
""", unsafe_allow_html=True)

    st.divider()
    st.markdown("### 🚀 Quick Info")
    st.caption("🎓 Student-focused analytics")
    st.caption("📊 Performance intelligence")
    st.caption("💡 Personalized guidance")
    st.caption("✨ Motivation")


st.markdown(
    '<div class="hero-badge">📊 STUDENT PERFORMANCE ANALYTICS</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-title">EduPredict AI 🎓</div>',
    unsafe_allow_html=True
)

st.markdown("""
<p class="hero-subtitle">
Understand your academic performance.<br>
Discover weak areas.<br>
Build better study habits.
</p>
""", unsafe_allow_html=True)

st.markdown("**Learn → Analyze → Improve → Grow 🚀**")

a, b, c, d = st.columns(4)
a.metric("📊 Prediction", "SMART")
b.metric("📈 Analytics", "LIVE")
c.metric("🎯 Guidance", "PERSONAL")
d.metric("💡 Motivation", "YES")


# ---------------- PREDICTOR ----------------

if page == "🏠 Predictor":

    st.header("🤖 Your Academic Buddy")
    st.write("Enter your academic information to analyze your current performance.")
    st.divider()

    name = st.text_input(
        "👤 Student Name",
        placeholder="Enter your name"
    )

    left, right = st.columns(2)

    with left:
        attendance = st.slider("📅 Attendance (%)", 0, 100, 80)
        study_hours = st.slider("📚 Daily Study Hours", 0.0, 12.0, 3.0, 0.5)
        internal = st.slider("📝 Internal Marks (%)", 0, 100, 70)

    with right:
        assignment = st.slider("📋 Assignment Score (%)", 0, 100, 70)
        previous = st.slider("🎯 Previous Exam Score (%)", 0, 100, 70)
        participation = st.slider("🙋 Class Participation (%)", 0, 100, 70)

    if st.button("🚀 ANALYZE MY PERFORMANCE 🚀", use_container_width=True):

        with st.spinner("Analyzing your academic profile..."):

            study_score = min(study_hours * 10, 100)

            score = (
                attendance * .18 +
                study_score * .17 +
                internal * .20 +
                assignment * .15 +
                previous * .20 +
                participation * .10
            )

            if score >= 80:
                result = "Excellent"
                emoji = "🏆"
                message = "Your academic habits are looking strong. Keep pushing forward!"
                mission = "Maintain your routine and challenge yourself with advanced topics."

            elif score >= 65:
                result = "Good"
                emoji = "🟢"
                message = "You are on the right track. A little more consistency can make you stronger."
                mission = "Strengthen your weakest area and stay consistent."

            elif score >= 50:
                result = "Average"
                emoji = "🟡"
                message = "You are making progress. Focus on your weakest areas step by step."
                mission = "Start with a simple daily routine and improve one area at a time."

            else:
                result = "Needs Improvement"
                emoji = "🔴"
                message = "This is only a starting point. Consistent effort can improve your result."
                mission = "Start with a simple daily routine and improve one area at a time."

            confidence = min(95, max(60, score))

        st.divider()
        st.header("🎉 Your Performance Result")

        r1, r2, r3 = st.columns(3)

        r1.metric("Prediction", f"{emoji} {result}")
        r2.metric("Smart Score", f"{score:.1f}%")
        r3.metric("Score Confidence", f"{confidence:.1f}%")

        st.progress(int(confidence))
        st.success(f"🤖 Academic Buddy: {message}")

        st.markdown('<div class="quote-box">', unsafe_allow_html=True)
        st.markdown("### ✨ MOTIVATION")
        st.markdown(f'### “{get_quote()}”')
        st.markdown("</div>", unsafe_allow_html=True)

        st.header("📊 Your Academic Profile")

        categories = [
            "Attendance",
            "Study",
            "Internal",
            "Assignment",
            "Previous",
            "Participation"
        ]

        values = [
            attendance,
            study_score,
            internal,
            assignment,
            previous,
            participation
        ]

        fig = go.Figure(
            go.Scatterpolar(
                r=values,
                theta=categories,
                fill="toself",
                name="Academic Profile"
            )
        )

        fig.update_layout(
            polar=dict(
                bgcolor="white",
                radialaxis=dict(visible=True, range=[0, 100])
            ),
            paper_bgcolor="rgba(0,0,0,0)",
            height=500,
            margin=dict(l=40, r=40, t=40, b=40),
            showlegend=False
        )

        st.plotly_chart(fig, use_container_width=True)

        st.header("📊 Academic Snapshot")

        s1, s2, s3, s4 = st.columns(4)
        s1.metric("📅 Attendance", f"{attendance}%")
        s2.metric("📚 Study", f"{study_hours} hrs")
        s3.metric("📝 Internal", f"{internal}%")
        s4.metric("🎯 Previous", f"{previous}%")

        st.header("💡 Personalized Advice")

        c1, c2 = st.columns(2)

        with c1:
            if attendance < 75:
                st.warning("📅 Attendance needs improvement.")
            else:
                st.success("📅 Attendance is looking good!")

            if study_hours < 3:
                st.warning("📚 Try adding 30–60 minutes of focused study.")
            else:
                st.success("📚 Good study commitment!")

        with c2:
            if internal < 60:
                st.warning("📝 Spend more time preparing for internal exams.")
            else:
                st.success("📝 Internal performance is good!")

            if assignment < 60:
                st.warning("📋 Try completing assignments earlier.")
            else:
                st.success("📋 Assignment performance is good!")

        st.header("🚀 Your Next Mission")
        st.info(f"🎯 {mission}")

        st.success(
            "🌟 You don't have to be perfect. "
            "You just have to keep improving."
        )

        st.session_state.history.append({
            "Student": name or "Anonymous",
            "Attendance": attendance,
            "Study Hours": study_hours,
            "Internal": internal,
            "Assignment": assignment,
            "Previous Score": previous,
            "Participation": participation,
            "Prediction": result,
            "Score": round(score, 2),
            "Confidence": round(confidence, 2)
        })


# ---------------- DASHBOARD ----------------

elif page == "📊 Dashboard":

    st.header("📊 Student Analytics Dashboard")

    if not st.session_state.history:
        st.info("📭 No analysis yet. Go to Predictor and run your first analysis.")

    else:
        df = pd.DataFrame(st.session_state.history)

        a, b, c, d = st.columns(4)

        a.metric("👨‍🎓 Analyses", len(df))
        b.metric("📅 Avg Attendance", f"{df['Attendance'].mean():.1f}%")
        c.metric("📚 Avg Study", f"{df['Study Hours'].mean():.1f} hrs")
        d.metric("🏆 Avg Score", f"{df['Score'].mean():.1f}%")

        st.divider()
        st.subheader("📈 Performance Comparison")

        st.bar_chart(
            df[
                [
                    "Attendance",
                    "Internal",
                    "Assignment",
                    "Previous Score",
                    "Participation"
                ]
            ]
        )

        st.subheader("🗂️ Analysis Records")

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        st.download_button(
            "⬇️ Download CSV Report",
            df.to_csv(index=False),
            "edupredict_report.csv",
            "text/csv",
            use_container_width=True
        )

        if st.button("🗑️ Clear Dashboard"):
            st.session_state.history = []
            st.rerun()


# ---------------- STUDY ADVISOR ----------------

elif page == "💡 Study Advisor":

    st.header("💡 Smart Study Advisor")
    st.write("Choose an area and get a simple action plan.")

    goal = st.selectbox(
        "🎯 What do you want to improve?",
        [
            "Marks",
            "Attendance",
            "Study Habits",
            "Exam Preparation",
            "Assignments",
            "Consistency"
        ]
    )

    plans = {
        "Marks": [
            "📝 Practice questions daily.",
            "🧠 Focus on weak topics.",
            "🔎 Review mistakes.",
            "🎯 Take practice tests."
        ],
        "Attendance": [
            "📅 Attend classes regularly.",
            "⏰ Maintain a routine.",
            "📚 Complete missed work."
        ],
        "Study Habits": [
            "📱 Remove distractions.",
            "⏱️ Study in focused sessions.",
            "☕ Take short breaks.",
            "🧠 Practice instead of only reading."
        ],
        "Exam Preparation": [
            "📋 Create a revision plan.",
            "🎯 Start difficult topics first.",
            "📝 Practice questions.",
            "🔁 Revise regularly."
        ],
        "Assignments": [
            "📅 Start early.",
            "📖 Understand the question.",
            "🔍 Check your work.",
            "⏰ Submit on time."
        ],
        "Consistency": [
            "🌱 Start small.",
            "📅 Set daily goals.",
            "📈 Track your progress.",
            "🔥 Keep going."
        ]
    }

    st.subheader(f"🚀 Your {goal} Plan")

    for item in plans[goal]:
        st.info(item)

    st.divider()
    st.success(f"🌟 Motivation: “{get_quote()}”")


# ---------------- ABOUT ----------------

else:

    st.header("ℹ️ About EduPredict AI")

    st.write("""
EduPredict AI is a student performance analytics platform
built with Python and Streamlit.

It analyzes academic information and provides performance
insights, study guidance and motivation.
""")

    st.divider()

    c1, c2 = st.columns(2)

    with c1:
        st.subheader("🛠️ Technologies")
        st.info("""
🐍 Python

🎨 Streamlit

📊 Pandas

📈 Plotly
""")

    with c2:
        st.subheader("✨ Features")
        st.info("""
📊 Performance Prediction

📈 Analytics Dashboard

💡 Study Advisor

🤖 Motivation

📊 Performance Graph

⬇️ CSV Report

🔐 No API Key
""")

    st.divider()

    st.success("🎓 Learn • Analyze • Improve • Grow 🚀")

    st.warning(
        "⚠️ Educational project only. "
        "Results should not be treated as official academic results."
    )


st.divider()

st.markdown("""
<div class="footer">
🎓 EduPredict AI • 📊 Smart Analytics • 💡 Student Guidance
</div>
""", unsafe_allow_html=True)