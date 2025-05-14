import streamlit as st
from file_handler import save_uploaded_file, read_file
from agent import enhance_code



st.set_page_config(page_title="Code Assistant Agent")
st.title("🧠 Context-Aware Code Assistant")

uploaded_file = st.file_uploader("Upload your code file", type=["py"])

if uploaded_file:
    file_path = save_uploaded_file(uploaded_file)
    original_code = read_file(file_path)
    st.subheader("Original Code")
    st.code(original_code, language="python")

    if st.button("Enhance with Agent"):
        enhanced_code = enhance_code(original_code)
        st.subheader("Enhanced Code")
        st.code(enhanced_code, language="python")
