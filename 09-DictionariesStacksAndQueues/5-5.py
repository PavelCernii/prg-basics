paragraph = "cat dog mouse cat rat cat mouse"

words_split = paragraph.split()

word_count = {}

for word in words_split:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word, count in word_count.items():
    print(f'{word}:{count}')