RISK_PHRASES = [
    "may suggest",
    "possibly",
    "could indicate",
    "might improve",
    "appears to"
]

def detect_hallucinations(text):

    findings = []

    for phrase in RISK_PHRASES:
        if phrase in text.lower():
            findings.append(
                f"Potential vague wording detected: '{phrase}'"
            )

    return findings