import streamlit as st

st.title("session_state vs plain variable")

# A plain variable: reset to 0 on every rerun, then becomes 1
counter = 0
counter += 1

# session_state: created once per browser session, survives reruns
if "clicks" not in st.session_state:
    st.session_state.clicks = 0

if st.button("Click me"):
    st.session_state.clicks += 1

st.write(f"Plain variable `counter`: **{counter}**")
st.write(f"`st.session_state.clicks`: **{st.session_state.clicks}**")

# Also print to the terminal so you can watch each rerun
print(f"RERUN -> counter={counter}, clicks={st.session_state.clicks}", flush=True)