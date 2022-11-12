import re

# Thiago Braga de Melo
# UFAM - Universidade Federal do Amazonas
# ICOMP - Instituto de Computação
# Prática em Banco de Dados - 2022
def read_file(path):
    file_read = open(path)
    return file_read


class Collection:
    def __init__(self, path):
        self.total_words = 0  # type: ignore
        self.top10 = dict()
        self.path = path

    def total_words_v2(self):
        count_words_v2 = 0
        my_file = read_file(self.path)
        for line in my_file:
            # each line is a different word
            count_words_v2 += 1

        print(
            "Total de palavras diferentes na Versão 2 do contador de palavras:",
            count_words_v2,
        )

    def top10_words_v2(self):
        my_file = read_file(self.path)
        for line in my_file:
            # split line to create dict(word, n_occurrences)
            self.top10[line.split()[0]] = line.split()[1]

        # now to access = dict[word]
        # order dict by value (n_occurrences)
        top10_sorted = sorted(
            self.top10.items(), key=lambda item: int(item[1]), reverse=True
        )

        # interate in top10 words
        position = 1
        print("Top 10 palavras que mais ocorrem na coleção: \n")
        for item in top10_sorted:
            if position <= 10:
                print(position, " - Palavra:", item[0], "com ", item[1], "repeticoes.")
            else:
                break
            position += 1


if __name__ == "__main__":
    # create collection with path to output file
    my_collection = Collection("./output-shakespeare/part-00000")

    # call methods
    my_collection.total_words_v2()
    my_collection.top10_words_v2()
