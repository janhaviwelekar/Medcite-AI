import re

class TextPreprocessor:

    def clean_text(self, text):

        text = re.sub(r'\n', ' ', text)
        text = re.sub(r'\s+', ' ', text)

        return text.strip()