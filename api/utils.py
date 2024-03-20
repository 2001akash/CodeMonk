# api/utils.py

import re

def tokenize_paragraphs(text):
    return re.split(r'\n{2,}', text)