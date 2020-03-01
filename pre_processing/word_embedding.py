import os
import zipfile

class WordEmbedding():

    TWEET_GLOVE_DIR = "glove.twitter.27B.25d.txt"
    
    def __init__(self, max_dictionary_size=50000):

        self.embedding_dictionary = {}
        self.max_dictionary_size = max_dictionary_size

        module_path = os.path.abspath(__file__)
        self.dictionary_path = os.path.join(
            os.path.dirname(module_path),
            "resources", self.TWEET_GLOVE_DIR)

    def load_embedding_dictionary(self, file_path):

        self.embedding_dictionary = {}
        embeding = []
        if ".zip/" in file_path:
            archive_path = os.path.abspath(file_path)

            split = archive_path.split(".zip/")

            archive_path = split[0] + ".zip"
            path_inside = split[1]

            archive = zipfile.ZipFile(archive_path, "r")
            embeddings = archive.read(path_inside).decode("utf8").split("\n")

        else:
            embeddings = open(file_path, "r", encoding="utf8").read().split("\n")

        for index, row in enumerate(embeddings):

            split = row.split(" ")

            if index == self.max_dictionary_size:
                return

            self.embedding_dictionary[split[0]] = index

    def replace_tokens_with_index(self, token_list):
        index_list = []
        for token in token_list:

            token_index = self.embedding_dictionary.get(token, 1)
            index_list.append(token_index)

        return index_list

