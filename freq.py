from collections import defaultdict, Counter
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


def calculate_freq_3(sentence):
    return Counter(sentence.lower().split())



if __name__ == "__main__":
    print(calculate_freq("This is a simple text"))
    print(calculate_freq_2("This is a simple text text"))
    print(calculate_freq_3("This is a simple text text"))