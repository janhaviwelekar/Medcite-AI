def calculate_aeo_score(text):

    score = 50

    if "objective" in text.lower():
        score += 10

    if "results" in text.lower():
        score += 10

    if len(text.split(".")) > 5:
        score += 10

    if len(text.split()) > 150:
        score += 10

    return min(score, 100)