def count_words(text):
    return len(text.split())

def longest_to_shortest(text):
    words = text.split()
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) < len(words[j]):
                words[i], words[j] = words[j], words[i]
    return words

def alphabetically_ordered(text):
    words = text.split()
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if words[i].lower() > words[j].lower():
                words[i], words[j] = words[j], words[i]
    return words
