import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import streamlit as st


def plot_score_gauge(title, score):

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={'text': title},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'thickness': 0.3},
            'steps': [
                {'range': [0, 40], 'color': "#EF4444"},
                {'range': [40, 70], 'color': "#F59E0B"},
                {'range': [70, 100], 'color': "#10B981"}
            ]
        }
    ))

    st.plotly_chart(fig, use_container_width=True)


def plot_entity_chart(entities):

    if not entities:
        st.info("No medical entities detected.")
        return

    df = pd.DataFrame(entities)

    counts = df["type"].value_counts().reset_index()

    counts.columns = ["Entity Type", "Count"]

    fig = px.bar(
        counts,
        x="Entity Type",
        y="Count",
        title="Medical Entity Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)


def plot_heatmap(text):

    words = text.split()[:30]

    scores = [len(word) for word in words]

    df = pd.DataFrame({
        "Word": words,
        "Score": scores
    })

    fig = px.density_heatmap(
        df,
        x="Word",
        y="Score",
        title="Retrieval Heatmap"
    )

    st.plotly_chart(fig, use_container_width=True)