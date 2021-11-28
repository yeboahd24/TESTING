text = "that is the same as a string counted corrected and jumped"

def count_words_ended_with_ed(text):
    """
    Count the number of words in text that end with 'ed'
    """
    return len([word for word in text.split() if word.endswith('ed')])

print(count_words_ended_with_ed(text))


def display_words_ended_with_ed(text):
    """
    Display the words in text that end with 'ed'
    """
    for word in text.split():
        if word.endswith('ed'):
            print(word)
            
print(display_words_ended_with_ed(text))


def count_words_with_four_letters(text):
    """
    Count the number of words in text that have four letters
    """
    return len([word for word in text.split() if len(word) == 4])

print(count_words_with_four_letters(text))


arrays = [1,2,3,4,5,6,7,8,9,10]
