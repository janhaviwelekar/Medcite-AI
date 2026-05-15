import textstat

def semantic_clarity(text):

    score = 70

    avg_sentence_length = len(text.split()) / max(len(text.split(".")), 1)

    if avg_sentence_length < 25:
        score += 10

    if "conclusion" in text.lower():
        score += 10

    return min(score, 100)