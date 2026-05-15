import re

DISEASES = [
    "cancer",
    "diabetes",
    "covid",
    "hypertension",
    "tumor",
    "asthma"
]

DRUGS = [
    "aspirin",
    "ibuprofen",
    "paracetamol",
    "metformin"
]

TREATMENTS = [
    "chemotherapy",
    "radiation therapy",
    "immunotherapy",
    "surgery"
]

BIOMARKERS = [
    "protein",
    "gene",
    "biomarker",
    "mutation"
]

def extract_medical_entities(text):

    text_lower = text.lower()

    entities = []

    for disease in DISEASES:
        if disease in text_lower:
            entities.append({
                "word": disease,
                "type": "DISEASE"
            })

    for drug in DRUGS:
        if drug in text_lower:
            entities.append({
                "word": drug,
                "type": "DRUG"
            })

    for treatment in TREATMENTS:
        if treatment in text_lower:
            entities.append({
                "word": treatment,
                "type": "TREATMENT"
            })

    for biomarker in BIOMARKERS:
        if biomarker in text_lower:
            entities.append({
                "word": biomarker,
                "type": "BIOMARKER"
            })

    return entities