import re
def tokenize(text):
    clear_text = re.sub(r'[^\w\s-]', ' ', text)
    new_text = clear_text.split()
    return new_text