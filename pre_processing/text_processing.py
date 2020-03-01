import re
from nltk.tokenize import TweetTokenizer


class TextProcessor():

    def __init__(self):
        self.url_regex = r"https?:\/\/[^ ]+"
        self.tokenizer = TweetTokenizer(strip_handles=True, reduce_len=False, preserve_case=True)

    def clean_text(self, input_text):
        cleaned_text = re.sub(self.url_regex, "", input_text, flags=re.MULTILINE).strip()
        return cleaned_text

    def tokenize_text(self, input_text):

        tokens = self.tokenizer.tokenize(input_text)

        return tokens
