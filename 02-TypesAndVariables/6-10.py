###
# String manipulation

movie = "The Lord of the Rings: The Return of the King"

# display number of characters
print('Number of characters: ', len(movie))

# display title in capital letters
print('Title in capital letters: ', movie.upper() )

# display title in small letters
print('Title in small letters: ', movie.lower() )

# display how many times the vowel "e" appears in the title
print('Number of times "e" appears: ', movie.count('e'))

# display where in the text is the word "Lord"
print('Position of the word "Lord": ', movie.find('Lord'))

# display where in the text is the word "dragon"
print('Position of the word "dragon": ', movie.find('dragon'))