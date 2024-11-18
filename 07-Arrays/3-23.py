import MyText

text = "An apple a day keeps the doctor away"

print("Text:", text)
print("Number of words:", MyText.count_words(text))

longest_words = MyText.longest_to_shortest(text)
print("Words from the longest:", end=" ")
for word in longest_words:
    print(word, end=" ")

alphabetical_words = MyText.alphabetically_ordered(text)
print("\nWords ordered alphabetically:", end=" ")
for word in alphabetical_words:
    print(word, end=" ")
