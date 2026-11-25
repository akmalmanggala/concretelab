"""ConcreteLab — Streamlit Web Application.

Owner: Person 3 (Streamlit & UX Engineer)
Tasks: P3-01 s.d. P3-08
"""

import streamlit as st

st.set_page_config(
    page_title="ConcreteLab — Prediksi Kuat Tekan Beton",
    page_icon="🧱",
    layout="centered",
)

st.title("ConcreteLab")
st.caption("Estimasi Kuat Tekan Beton (MPa) berbasis Machine Learning")

st.info(
    "Skeleton aplikasi siap dijalankan. Form 8 fitur dan integrasi "
    "`predict_strength()` akan dibangun pada branch `feat/P3-streamlit-ui`."
)
