from collections import defaultdict, Counter
from string import punctuation


def calculate_freq(sentence):
    freq = {}
    for word in sentence.lower().split():
        if word is freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

def calculate_freq_2(sentence):
    freq = defaultdict(int)
    for word in sentence.lower().split():
        freq[word] += 1
    return freq


class FileFreqCounter:
    def __init__(self, path):
        self.path = path
        self.counter = Counter()
        self.symbols = set(punctuation)

    def read_lines(self):
        with open(self.path) as f:  # r , w , a - tryb otwarcia pliku read, write, append
            return [line.replace("]n", "") for line in f]
    def remove_punctuation(self, sentence):

        for ch in sentence:
            if ch in self.symbols:
                sentence = sentence.replace(ch, " ")
        return sentence
    def calculate_freq_3(self):
        sentences = self.read_lines()
        self.counter = Counter()
        for sentence in sentences:
            cleaned = self.remove_punctuation(sentence)
            self.counter += Counter(cleaned.lower().split())
        return self.counter
    def most_common(self, n=3):
        self.calculate_freq_3()
        return self.counter.most_common(n)



if __name__ == "__main__":
    file_counter = FileFreqCounter("story.txt")
    print(file_counter.most_common(5))
