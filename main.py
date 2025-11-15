# main.py
from datetime import datetime
import io
import pandas as pd
import streamlit as st
from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory, LangDetectException

# deterministic langdetect
DetectorFactory.seed = 0

st.set_page_config(page_title="Multilingual Translator", page_icon="🌍")
st.title("🌍 Multilingual Translator")

st.markdown(
    "Paste text in any language. "
    "This app will detect the language, translate it into English, "
    "and produce a short neutral suggested response."
)

# initialize session state keys if missing
if "query" not in st.session_state:
    st.session_state["query"] = ""
if "demo_input" not in st.session_state:
    st.session_state["demo_input"] = ""

col1, col2 = st.columns([3, 1])
with col1:
    # bind the text_area to session_state['query']
    query = st.text_area("Enter text to translate (any language):", value=st.session_state["query"], height=160, key="query")
with col2:
    save_toggle = st.checkbox("Enable CSV download", value=True)
    # Use an on_click callback to modify session_state safely
    def _clear_query() -> None:
        st.session_state["query"] = ""

    st.button("Clear input", on_click=_clear_query)

def detect_language(text: str) -> str:
    try:
        lang = detect(text)
        return lang
    except LangDetectException:
        return "unknown"

def translate_to_english(text: str) -> str:
    try:
        translated = GoogleTranslator(source='auto', target='en').translate(text)
        return translated
    except Exception as e:
        return f"[Translation error: {e}]"


# Main Translate action
if st.button("Translate") and st.session_state["query"].strip():
    query_text = st.session_state["query"]
    with st.spinner("Detecting language and translating..."):
        detected_lang = detect_language(query_text)
        translation = translate_to_english(query_text)

    st.subheader("🗣 Original Query")
    st.write(query_text)

    st.subheader("Detected language code")
    st.code(detected_lang)

    st.subheader("🇬🇧 English Translation")
    st.success(translation)

   

    if save_toggle:
        row = {
            "timestamp": datetime.utcnow().isoformat(),
            "original": query_text,
            "detected_lang": detected_lang,
            "translation": translation,
        }
        df = pd.DataFrame([row])
        csv_buffer = io.StringIO()
        df.to_csv(csv_buffer, index=False)

        st.download_button(
            label="Download CSV",
            data=csv_buffer.getvalue().encode("utf-8"),
            file_name=f"translation_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv",
        )

