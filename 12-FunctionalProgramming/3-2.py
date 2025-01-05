sentence = 'I completely agree with you'
words = sentence.split()
result = list(map(lambda x: len(x), words))
print(result)