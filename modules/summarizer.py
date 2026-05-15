def generate_summary(text):

    sentences = text.split(".")

    short_summary = ".".join(sentences[:2])

    return short_summary