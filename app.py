import streamlit as st
from modules.aeo_analysis import calculate_aeo_score
from modules.geo_analysis import calculate_geo_score
from modules.citation_score import calculate_citation_probability
from modules.semantic_analysis import semantic_clarity
from modules.hallucination_detector import detect_hallucinations
from modules.medical_ner import extract_medical_entities
from modules.summarizer import generate_summary
from modules.visualization import (
    plot_score_gauge,
    plot_entity_chart,
    plot_heatmap
)

st.set_page_config(
    page_title="MedCite AI",
    layout="wide",
    page_icon="🧬"
)

st.title("🧬 MedCite AI")
st.subheader("Optimize medical research for AI discoverability")

st.sidebar.header("Upload Medical Content")

uploaded_file = st.sidebar.file_uploader(
    "Upload TXT file",
    type=["txt"]
)

text_input = st.text_area(
    "Paste PubMed Abstract / Clinical Summary",
    height=300
)

content = ""

if uploaded_file:
    content = uploaded_file.read().decode("utf-8")

elif text_input:
    content = text_input

if content:

    st.success("Medical content loaded successfully!")

    col1, col2, col3 = st.columns(3)

    aeo_score = calculate_aeo_score(content)
    geo_score = calculate_geo_score(content)
    citation_prob = calculate_citation_probability(content)

    with col1:
        st.metric("AEO Score", f"{aeo_score}%")

    with col2:
        st.metric("GEO Score", f"{geo_score}%")

    with col3:
        st.metric("AI Citation Probability", f"{citation_prob}%")

    st.divider()

    st.subheader("📌 Medical Entity Coverage")

    entities = extract_medical_entities(content)
    st.write(entities)

    plot_entity_chart(entities)

    st.divider()

    st.subheader("⚠️ Hallucination Risk Zones")

    hallucinations = detect_hallucinations(content)

    for item in hallucinations:
        st.warning(item)

    st.divider()

    st.subheader("🧠 Semantic Clarity")

    semantic_score = semantic_clarity(content)

    st.progress(semantic_score / 100)

    st.write(f"Semantic Clarity Score: {semantic_score}%")

    st.divider()

    st.subheader("🤖 AI Summary Simulation")

    summary = generate_summary(content)

    st.info(summary)

    st.divider()

    st.subheader("🔥 Retrieval Heatmap")

    plot_heatmap(content)