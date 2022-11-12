import sys
import io
import re
import nltk

# import hashlib

nltk.download("stopwords", quiet=True)
from nltk.corpus import stopwords

punctuations = """!()-[]{};:'"\,<>./?@#$%^&*_~"""
stop_words = set(stopwords.words("english"))
input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding="latin1")

# Thiago Braga de Melo
# UFAM - Universidade Federal do Amazonas
# ICOMP - Instituto de Computação
# Prática em Banco de Dados - 2022

# code to conform v2 with initialize hash words
class Mapper:
    # initialize??
    def __init__(self):
        self.dic_word = dict()

    def close(self):
        # print all words in dictionary
        for term in self.dic_word.keys():
            print("%s\t%s" % (term, self.dic_word[term]))

    def mapper(self):
        # interate each line in doc input stream
        for line in input_stream:
            line = line.strip()
            line = re.sub(r"[^\w\s]", "", line)
            line = line.lower()

            # remove simbols
            for x in line:
                if x in punctuations:
                    line = line.replace(x, " ")

            words = line.split()
            for word in words:
                # no stop_words
                if word not in stop_words:
                    # pattern required
                    pattern = re.compile(r"[A-Za-z]+")
                    # check word in pattern
                    if re.fullmatch(pattern, word):
                        # hash words to dictionary
                        if word in self.dic_word.keys():
                            self.dic_word[word] = self.dic_word[word] + 1
                        else:
                            self.dic_word[word] = 1


if __name__ == "__main__":
    my_mapper = Mapper()
    my_mapper.mapper()
    my_mapper.close()
