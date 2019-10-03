import difflib
import cleanup_function
import os

# get user inputs directory for documents
user_input = input("Enter the path of first document: ")
user_input2 = input("Enter the path of second document: ")

# open and clean up document and store into string / list
assert os.path.exists(user_input), "No file found at, "+str(user_input)
x = open(user_input, 'r+')
sample1_string = cleanup_function.remove_punctuation(x.read())
pre_list1 = cleanup_function.sentence_translator(sample1_string).lower().split()
sample1_list = cleanup_function.remove_articles(pre_list1)
x.close()

assert os.path.exists(user_input2), "No file found at, "+str(user_input2)
y = open(user_input2, 'r+')
sample2_string = cleanup_function.remove_punctuation(y.read())
pre_list2 = cleanup_function.sentence_translator(sample2_string).lower().split()
sample2_list = cleanup_function.remove_articles(pre_list2)
y.close()

# compare strings to see if they are exact match or give similarity score based on list
s = difflib.SequenceMatcher(None, sample1_list, sample2_list)
print(s.ratio())
