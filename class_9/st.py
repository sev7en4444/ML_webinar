import time
from datetime import datetime

import streamlit as st


def log(msg):
    """Print to the terminal with a timestamp so you can watch every rerun."""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)


log("=== SCRIPT BODY RAN (line 1 to bottom) ===")


@st.cache_resource
def load_model():
    log("    >>> load_model() REALLY EXECUTED <<<")
    time.sleep(2)  # pretend this is a heavy model load
    return {"name": "dummy-model"}


model = load_model()
st.write(f"Model loaded: {model['name']}")

agree = st.checkbox("Include attendance")
log(f"    checkbox returned {agree}")

if st.button("Predict"):
    log("    button returned True")
    st.success("Prediction done!")
else:
    log("    button returned False")