"""This code take a string of raw text as input
and produce an array of int as an output.
"""
import json
import os

from pre_processing.text_processing import TextProcessor
from pre_processing.word_embedding import WordEmbedding

class PreProcessor():
    """Pre Processing class used to convert json file into index list"""

    def __init__(self, padding_size=20, max_dictionary_size=500000):

        self.text_processor = TextProcessor()
        self.embedding = WordEmbedding(max_dictionary_size=max_dictionary_size)

        self.embedding.load_embedding_dictionary(self.embedding.dictionary_path)

        self.padding_size = padding_size

    def pre_process_text(self, text):

        cleaned_text = self.text_processor.clean_text(text)
        tokens = self.text_processor.tokenize_text(cleaned_text)
        print(tokens)
        embeding_indexes = self.embedding.replace_tokens_with_index(tokens)

        padded_indexes = self.pad_sequence(embeding_indexes)

        return padded_indexes

    def pad_sequence(self, input_sequence):
        """Step 4 pad_sequence"""

        sequence = input_sequence[-self.padding_size:]

        if len(sequence) < self.padding_size:

            pad_sequence = [0]*(self.padding_size - len(sequence))
            sequence += pad_sequence

        return sequence

# TEST CASE
# Read_data
# S = '{"text": "@my_handler here is my tweet http://www.columbia.com"}'
# input_text = json.loads(S)["text"]
# print(input_text)

# with open(data_dir+'text.json') as f:
# data_raw = json.load(f)

# Main function
# pre_processing = PreProcessor()
# print(pre_processing.pre_process_text(input_text))
# print(pre_processing.)
