
# dictionary of contractions and translation function

contractions = {
    "could've": "could have",
    "can't": "cannot",
    "couldn't": "could not",
    "didn't": "did not",
    "doesn't": "does not",
    "don't": "do not",
    "hadn't": "had not",
    "hasn't": "has not",
    "haven't": "have not",
    "shouldn't": "should not",
    "should've": "should have",
    "you'll": "you will",
    "we'd": "we had",
    "we'll": "we will",
    "we've": "we have",
    "weren't": "were not",
    "won't": "will not",
    "wouldn't": "would not",
    "would've": "would have",
    "you're": "you are",
    "you've": "you have",
}


def remove_punctuation(text):
    for char in text:
        if char in ".!?,":
            text = text.replace(char, "")
    return text


def sentence_translator(text):
    for word in text.split():
        if word.lower() in contractions:
            text = text.replace(word, contractions[word.lower()])
    return text


def remove_articles(my_list):
    i = 0
    while i < len(my_list):
        if my_list[i] == "the" or my_list[i] == "a" or my_list[i] == "an":
            del my_list[i]
            i = i
        else:
            i = i + 1
    return my_list
