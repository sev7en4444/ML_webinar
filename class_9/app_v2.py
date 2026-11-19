import streamlit as st

st.title("🎓 Will this student pass?")

print("Streamlit app is running...")

hours = st.slider("Hours studied", 0.0, 10.0, 5.0, step=0.1)
attendance = st.slider("Attendance %", 40, 100, 75)
prev_marks = st.slider("Previous marks", 0, 100, 60)
print("Streamlit app is running...")
st.write("You chose:", hours, attendance, prev_marks)
print("Streamlit app is running...")