def calculate_citation_probability(text):

    score = 40

    scientific_terms = [
        "study",
        "trial",
        "evidence",
        "clinical",
        "patients"
    ]

    for term in scientific_terms:
        if term in text.lower():
            score += 10

    return min(score, 100)