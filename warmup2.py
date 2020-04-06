def letter_to_number(letter):
    '''Takes in a letter and returns the numerical location of that number in the alphabet'''
    return ord(letter.lower()) - 96

def is_triangle_num(number):
    '''Takes in a int and returns a boolean value representing if the number is a triangle number'''
    total = 0
    base = 0
    while total <= number:
        total = total + base
        if (total == number):
            return True
        base += 1
    return False

def is_triangle_word(word):
    '''Takes in a string and returns a boolean value of whether the words letters add up to a triangle number'''
    total = 0
    for letter in word:
        total += letter_to_number(letter.lower())
    if is_triangle_num(total):
        return True
    else:
        return False

with open('/usr/share/dict/words') as f:
    words = f.read().strip().split('\n')

triangle_words =[word for word in words if is_triangle_word(word)]
print(f"The number of triangle words is {len(triangle_words)}")