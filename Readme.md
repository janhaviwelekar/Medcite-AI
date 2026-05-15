# 🧬 MedCite AI — AI Discoverability Engine for Medical Research

> Optimize medical research for AI retrieval, semantic understanding, and generative search visibility.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32-red?logo=streamlit)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-yellow?logo=huggingface)
![Domain](https://img.shields.io/badge/Domain-Healthcare%20AI-brightgreen)
![CPU Friendly](https://img.shields.io/badge/GPU-Not%20Required-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 What is MedCite AI?

MedCite AI is an AI-powered semantic intelligence platform that evaluates how effectively medical research content can be retrieved, understood, and cited by AI systems such as ChatGPT, Gemini, Perplexity, and Claude.

Most medical content is written for human readers — not optimized for semantic retrieval, generative search, or LLM summarization. As a result:

- Important studies may not surface in AI-powered search
- Vague conclusions increase the risk of AI hallucination
- Clinical findings become difficult for LLMs to interpret correctly

MedCite AI bridges this gap by combining **GEO**, **AEO**, biomedical NLP, and semantic embeddings into a single, practical dashboard.

---

## 💡 Why This Idea?

Modern AI systems increasingly influence healthcare search, scientific discovery, and clinical information retrieval. Yet very few tools exist to help optimize medical research specifically for AI discoverability.

MedCite AI explores an emerging category: **AI-native scientific content optimization** — helping researchers and clinicians understand how AI systems interpret their work, and where that interpretation may break down.

---

## ✨ Key Features

- **Medical AEO Score** — Measures answer extraction quality, direct response clarity, and FAQ-style answerability for AI assistants
- **GEO Score** — Evaluates semantic richness, retrievability, contextual completeness, and embedding consistency for generative AI systems
- **AI Citation Probability** — Predicts likelihood of ChatGPT, Perplexity, and Gemini citing or using the content in generated answers
- **Biomedical Entity Recognition** — Detects diseases, drugs, biomarkers, treatments, patient populations, and outcomes using HuggingFace NER models
- **Hallucination Risk Detection** — Identifies vague claims, unsupported conclusions, and ambiguous wording (e.g. "may suggest", "possibly associated")
- **Semantic Clarity Analysis** — Measures chunk independence, scientific readability, and contextual completeness for RAG pipelines
- **AI Summary Simulation** — Generates AI-style summaries, retrieval previews, and LLM-like response previews
- **Retrieval Heatmap** — Visualizes semantically important sections and retrieval-dense sentences

---

## 🤖 Hugging Face Models Used

| Model | Purpose |
|---|---|
| `sentence-transformers/all-MiniLM-L6-v2` | Semantic similarity, GEO scoring, retrieval analysis |
| `facebook/bart-large-cnn` | AI summary generation and retrieval previews |
| `facebook/bart-large-mnli` | Zero-shot classification, hallucination detection, scientific confidence analysis |
| `d4data/biomedical-ner-all` | Biomedical named entity recognition (diseases, drugs, treatments, biomarkers) |

All models run on CPU — no GPU required.

---

## 🏗️ Architecture

```
Medical Research Input
(PubMed / Clinical Trial / Article)
              │
              ▼
┌──────────────────────────────────┐
│      Input Processing Layer      │
│   TXT Upload + Text Cleaning     │
└──────────────────┬───────────────┘
                   │
                   ▼
┌──────────────────────────────────┐
│    Biomedical NLP Pipeline       │
│   Hugging Face Transformers      │
│   • NER  • Summarization         │
│   • Classification               │
└──────────────────┬───────────────┘
                   │
                   ▼
┌──────────────────────────────────┐
│   Semantic Intelligence Layer    │
│   • AEO Score  • GEO Score       │
│   • Citation Probability         │
│   • Semantic Clarity             │
│   • Hallucination Detection      │
└──────────────────┬───────────────┘
                   │
                   ▼
┌──────────────────────────────────┐
│     Visualization Engine         │
│   Plotly + Streamlit Dashboard   │
└──────────────────────────────────┘
```

---

## 📁 Project Structure

```
MedCite-AI/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
│
├── sample_data/
│   ├── sample_abstract.txt
│   └── clinical_trial.txt
│
├── modules/
│   ├── aeo_analysis.py
│   ├── geo_analysis.py
│   ├── citation_score.py
│   ├── semantic_analysis.py
│   ├── hallucination_detector.py
│   ├── medical_ner.py
│   ├── summarizer.py
│   └── visualization.py
│
├── utils/
│   ├── text_cleaner.py
│   ├── chunking.py
│   └── helpers.py
│
└── styles/
    └── custom_css.py
```

---

## ⚙️ Installation

### Prerequisites

- Python 3.11
- pip

### Setup

```bash
# 1. Clone the repository
git clone https://github.com/janhaviwelekar/MedCite-AI.git

# 2. Navigate to the project folder
cd MedCite-AI


# 3. Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Running the Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```
http://localhost:8501
```

---

## 📋 Example Input / Output

### Input

```
This clinical study evaluates the effectiveness of a novel biomarker-driven 
treatment for lung cancer patients. Results indicate improved survival outcomes 
and reduced recurrence rates. Further clinical validation is required.
```

### Output

```
Medical AEO Score          : 84%
GEO Score                  : 88%
AI Citation Probability    : 81%

Detected Entities:
  - Lung Cancer
  - Biomarker
  - Clinical Treatment

Hallucination Risk:
  - "Further clinical validation is required"

Semantic Clarity           : High

AI Summary:
  "This study demonstrates promising survival improvements using 
   biomarker-guided treatment approaches for lung cancer patients."
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| Backend | Python |
| NLP Framework | Hugging Face Transformers |
| Embeddings | Sentence Transformers |
| ML Utilities | scikit-learn |
| Visualization | Plotly |
| Data Handling | pandas, numpy |
| Deep Learning | PyTorch (CPU) |

---

## ⚠️ Assumptions

- Input content is English medical text
- User provides clean, textual medical content (PubMed abstracts, clinical trial summaries, healthcare articles)
- CPU-only inference environment
- Lightweight local execution — no cloud GPU required

---

## 🚧 Limitations

- Not intended for medical diagnosis or clinical decision-making
- Scores are heuristic-based and not a substitute for expert peer review
- Long-document support is limited in v1
- No vector database integration in v1
- No medical fact verification system

---

## 🔭 Future Improvements

- [ ] PDF research paper ingestion
- [ ] Clinical RAG benchmarking
- [ ] Multi-document semantic comparison
- [ ] Vector database integration (FAISS / Pinecone)
- [ ] Retrieval ranking optimization
- [ ] AI indexing recommendations
- [ ] Medical citation graph visualization
- [ ] Fine-tuned healthcare-specific embeddings

---

## 👤 Author

Built as part of the **Absolv Applied AI Technical Assessment**.
JANHAVI WELEKAR- SHRI RAMDEOBABA COLLEGE OF ENGINEERING & MANAGEMENT

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
