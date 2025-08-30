import streamlit as st

# ================= Profile Data =================
profile = {
    "Education": {
        "Matric": {"Year": "2018", "Marks": "767/1100", "Subjects": ["Math", "Physics", "Chemistry", "Computer Science"]},
        "Intermediate": {"Year": "2020", "Marks": "571/1100", "Subjects": ["Math", "Physics", "Computer Science"]},
        "Bachelor": {"Year": "2028", "CGPA": "2.48/4.0", "Subjects": ["Computer Science"]},
    },
    "Professional Skills": ["Python", "SQL", "Machine Learning", "Deep Learning", "Data Science", "Power BI", "Tableau"],
    "Soft Skills": ["Problem Solving", "Critical Thinking", "Communication", "Anger Management"],
    "Hobbies": ["Reading Books"]
}

# ================= Streamlit Page Config =================
st.set_page_config(page_title="Jiya - Personal Chatbot", page_icon="👩", layout="wide")

# ================= Title =================
st.markdown(
    """
    <h2 style="text-align:center;">👩 Jiya - Your Personal AI Chatbot</h2>
    <p style="text-align:center; color:gray;">Ask me anything about your education, skills, or hobbies.</p>
    """,
    unsafe_allow_html=True
)

# ================= Sidebar (Profile Card) =================
with st.sidebar:
    st.header("📌 Profile Overview")

    st.subheader("🎓 Education")
    for level, details in profile["Education"].items():
        if "Marks" in details:
            st.markdown(
                f"**{level}** ({details['Year']})  \n"
                f"Marks: {details['Marks']}  \n"
                f"Subjects: {', '.join(details['Subjects'])}"
            )
        elif "CGPA" in details:
            st.markdown(
                f"**{level}** ({details['Year']})  \n"
                f"CGPA: {details['CGPA']}  \n"
                f"Subjects: {', '.join(details['Subjects'])}"
            )

    st.subheader("💼 Professional Skills")
    st.markdown(", ".join(profile["Professional Skills"]))

    st.subheader("🌱 Soft Skills")
    st.markdown(", ".join(profile["Soft Skills"]))

    st.subheader("📚 Hobbies")
    st.markdown(", ".join(profile["Hobbies"]))

# ================= Chatbot Memory =================
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# ================= Chat Input =================
user_input = st.chat_input("💬 Type your question here...")

if user_input:
    response = ""
    query = user_input.lower()

    # Education Queries
    if "education" in query:
        response = "Here’s a summary of your education: " + "; ".join(
            [f"{lvl} ({d['Year']}, {d.get('Marks', d.get('CGPA'))})" for lvl, d in profile["Education"].items()]
        )
    elif "matric" in query:
        d = profile["Education"]["Matric"]
        response = f"You completed Matric in {d['Year']} with {d['Marks']} in subjects: {', '.join(d['Subjects'])}."
    elif "intermediate" in query:
        d = profile["Education"]["Intermediate"]
        response = f"You completed Intermediate in {d['Year']} with {d['Marks']} in subjects: {', '.join(d['Subjects'])}."
    elif "bachelor" in query:
        d = profile["Education"]["Bachelor"]
        response = f"You are pursuing Bachelor (Year: {d['Year']}) with CGPA {d['CGPA']} in subjects: {', '.join(d['Subjects'])}."

    # Skills Queries
    elif "professional skill" in query or "technical skill" in query:
        response = "Your professional skills are: " + ", ".join(profile["Professional Skills"])
    elif "soft skill" in query:
        response = "Your soft skills are: " + ", ".join(profile["Soft Skills"])

    # Hobbies Queries
    elif "hobby" in query or "hobbies" in query:
        response = "Your hobbies include: " + ", ".join(profile["Hobbies"])

    # Default Response
    else:
        response = "I'm Jiya 👩, your personal chatbot! You can ask me about your education, skills, or hobbies."

    st.session_state["chat_history"].append(("You", user_input))
    st.session_state["chat_history"].append(("Jiya", response))

# ================= Chat Display (WhatsApp Style) =================
for sender, msg in st.session_state["chat_history"]:
    if sender == "You":
        st.markdown(
            f"<div style='text-align:right; color:white; background:#25D366; padding:10px; "
            f"border-radius:12px; margin:5px; max-width:70%; float:right; clear:both;'>{msg}</div>",
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"<div style='text-align:left; color:black; background:#EAEAEA; padding:10px; "
            f"border-radius:12px; margin:5px; max-width:70%; float:left; clear:both;'>👩 <b>Jiya:</b> {msg}</div>",
            unsafe_allow_html=True,
        )
