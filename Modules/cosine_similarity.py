import re, math
from collections import Counter
import fuzzywuzzy.fuzz

WORD = re.compile(r'\w+')


def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)


def givKeywordsValue(text1, text2):
    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)
    cosine = round(get_cosine(vector1, vector2),2)*100
    kval = 0
    if cosine > 90:
        kval = 1
    elif cosine > 80:
        kval = 2
    elif cosine > 60:
        kval = 3
    elif cosine > 40:
        kval = 4
    elif cosine > 20:
        kval = 5
    else:
        kval = 6
    return kval

#
# text1 = "Encapsulation is an object-oriented programming concept that combines data and the functions that manipulate it into a single unit called a class. This process binds together the relevant data and its associated functions, while also hiding the implementation details from the user through data hiding. By encapsulating data, we can prevent outside interference and misuse, while also achieving a strong form of abstraction through the selective exposure of only relevant data."

# text2 = "Encapsulation is an object-oriented programming concept that combines data and the functions that manipulate it into a single unit called a class. This process binds together the relevant data and its associated functions, while also hiding the implementation details from the user through data hiding. By encapsulating data, we can prevent outside interference and misuse, while also achieving a strong form of abstraction through the selective exposure of only relevant data."

# a = givKeywordsValue(text1=text1, text2=text2)
# print(a)
# print('Fuzzywuzzy: ', fuzzywuzzy.fuzz.token_set_ratio(vector1,vector2))