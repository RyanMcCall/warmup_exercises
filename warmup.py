def letter_to_number(letter):
    return ord(letter.lower()) - 96

def first_equals_rest(word):
    first_letter = letter_to_number(word[0])
    total = 0
    for letter in word[1:len(word)]:
        total += letter_to_number(letter.lower())
    if total == first_letter:
        return True
    else:
        return False

with open('/usr/share/dict/words') as f:
    words = f.read().split('\n')

five_letter_words = [word for word in words if len(word) == 5]

words_where_first_equals_rest = [word for word in five_letter_words if first_equals_rest(word)]
print(words_where_first_equals_rest)