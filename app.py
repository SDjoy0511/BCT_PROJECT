import streamlit as st
import os
import dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load env
dotenv.load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")

# Page setup
st.set_page_config(page_title="AI Interview Simulator", layout="wide")
st.title("🎯 AI Interview Simulator with Personality-Based Feedback")

# Session Memory
if "chat" not in st.session_state:
    st.session_state.chat = []
if "level" not in st.session_state:
    st.session_state.level = "Easy"

# Sidebar
st.sidebar.header("Interview Setup")
domain = st.sidebar.selectbox("Select Domain", ["Python", "Java", "Machine Learning", "Web Development", "Android"])
role = st.sidebar.selectbox("Interviewer Role", ["HR", "Technical", "Manager"])

st.sidebar.write("Difficulty Level:", st.session_state.level)

# LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Prompt Builder
def build_prompt(domain, role, difficulty, history, user_answer=""):
    if user_answer:
        return f"""
You are an expert interviewer acting as a {role} interviewer for {domain}.

Evaluate the following candidate answer:

Answer:
{user_answer}

Give:
1. Score out of 10 for:
   - Technical Accuracy
   - Clarity
   - Confidence
2. Strengths
3. Weaknesses
4. Improvement tips

Keep professional tone.
"""
    else:
        return f"""
You are a professional {role} interviewer conducting a {difficulty} level interview in {domain}.

Ask ONE realistic interview question.

If difficulty is Easy → basic fundamentals.
If Medium → scenario based.
If Hard → deep technical + design thinking.

Only ask question, nothing else.
"""

# Ask Question
if st.button("Ask Next Question"):
    prompt = build_prompt(domain, role, st.session_state.level, st.session_state.chat)
    question = llm.invoke(prompt)
    st.session_state.chat.append(("Interviewer", question.content))

# Display Chat
for role_, msg in st.session_state.chat:
    if role_ == "Interviewer":
        st.chat_message("assistant").write(msg)
    else:
        st.chat_message("user").write(msg)

# Answer Input
answer = st.chat_input("Type your answer")

if answer:
    st.session_state.chat.append(("Candidate", answer))

    eval_prompt = build_prompt(domain, role, st.session_state.level, st.session_state.chat, answer)
    evaluation = llm.invoke(eval_prompt)

    st.subheader("📊 Interview Evaluation")
    st.success(evaluation.content)

    # Dynamic Difficulty Upgrade
    if st.session_state.level == "Easy":
        st.session_state.level = "Medium"
    elif st.session_state.level == "Medium":
        st.session_state.level = "Hard"

# Final Performance Summary
if st.button("End Interview"):
    summary_prompt = f"""
Analyze this full interview:

{st.session_state.chat}

Give:
1. Overall Interview Score / 100
2. Technical Strengths
3. Weak Areas
4. Personalized Improvement Roadmap (7 days plan)
"""

    summary = llm.invoke(summary_prompt)
    st.subheader("🏆 Final Interview Performance Report")
    st.info(summary.content)