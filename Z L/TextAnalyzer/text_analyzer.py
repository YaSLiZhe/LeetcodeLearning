def word_count(text):
    words = text.split()
    return len(words)


def word_frequency(text):
    fre = {}
    words = text.split()
    for word in words:
        if word in fre:
            fre[word] += 1
        else:
            fre[word] = 1
    return fre


with open("TextAnalyzer\sample_text.txt", "r") as file:
    text = file.read()
    counts = word_count(text)
    # Word frequency
    frequencies = word_frequency(text)
    print('The text is', text)
    print('The number of the text is ', counts)
    print("\nWord Frequencies:", frequencies)
