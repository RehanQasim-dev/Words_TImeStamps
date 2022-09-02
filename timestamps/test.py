from string import ascii_letters
characters="0123456789"+ascii_letters
word='U.S.,'
def extract_word(word):
    for i in range(int(len(word)/2+1)):
        if word[0] not in characters:
            word=word[1:]
        if word[-1] not in characters:
            word=word[0:-1]
    return word.lower()
extract_word(word)